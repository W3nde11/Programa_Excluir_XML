import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

# ---------------- LOG ----------------
def escrever_log(msg):
    with open("log_exclusao.txt", "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()} - {msg}\n")

# ---------------- CARREGAR EXCEL ----------------
def carregar_chaves(caminho_excel):
    try:
        df = pd.read_excel(caminho_excel)

        if "CHAVE" not in df.columns:
            raise Exception("Coluna 'CHAVE' não encontrada.")

        chaves = df["CHAVE"].astype(str).str.strip().tolist()
        return chaves

    except Exception as e:
        messagebox.showerror("Erro", str(e))
        return []

# ---------------- EXCLUIR XML ----------------
def excluir_xmls(pasta, chaves):
    excluidos = 0
    nao_encontrados = 0

    arquivos = os.listdir(pasta)

    for chave in chaves:
        encontrado = False

        for arquivo in arquivos:
            if chave in arquivo and arquivo.lower().endswith(".xml"):
                caminho_arquivo = os.path.join(pasta, arquivo)

                try:
                    os.remove(caminho_arquivo)
                    escrever_log(f"EXCLUÍDO: {arquivo}")
                    excluidos += 1
                    encontrado = True
                except Exception as e:
                    escrever_log(f"ERRO ao excluir {arquivo}: {e}")

        if not encontrado:
            escrever_log(f"NÃO ENCONTRADO: {chave}")
            nao_encontrados += 1

    return excluidos, nao_encontrados

# ---------------- BOTÕES ----------------
def selecionar_excel():
    caminho = filedialog.askopenfilename(
        filetypes=[("Arquivos Excel", "*.xlsx")]
    )
    entrada_excel.delete(0, tk.END)
    entrada_excel.insert(0, caminho)

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    entrada_pasta.delete(0, tk.END)
    entrada_pasta.insert(0, pasta)

def iniciar_processo():
    excel = entrada_excel.get()
    pasta = entrada_pasta.get()

    if not excel or not pasta:
        messagebox.showwarning("Aviso", "Selecione o Excel e a pasta.")
        return

    escrever_log("===== INÍCIO DO PROCESSO =====")

    chaves = carregar_chaves(excel)

    if not chaves:
        return

    excluidos, nao_encontrados = excluir_xmls(pasta, chaves)

    escrever_log("===== FIM DO PROCESSO =====")

    messagebox.showinfo(
        "Finalizado",
        f"Arquivos excluídos: {excluidos}\n"
        f"Não encontrados: {nao_encontrados}"
    )

# ---------------- INTERFACE ----------------
janela = tk.Tk()
janela.title("Exclusão de XML NFe")
janela.geometry("500x220")
janela.resizable(False, False)

tk.Label(janela, text="Planilha Excel:").pack(pady=5)
entrada_excel = tk.Entry(janela, width=60)
entrada_excel.pack()

tk.Button(janela, text="Selecionar Excel", command=selecionar_excel).pack(pady=5)

tk.Label(janela, text="Pasta dos XMLs:").pack(pady=5)
entrada_pasta = tk.Entry(janela, width=60)
entrada_pasta.pack()

tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta).pack(pady=5)

tk.Button(
    janela,
    text="INICIAR EXCLUSÃO",
    bg="red",
    fg="white",
    height=2,
    command=iniciar_processo
).pack(pady=15)


janela.mainloop()