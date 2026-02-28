# 📦 Programa_Excluir_XMLs

Este documento apresenta o **Programa_Excluir_XMLs**, uma solução desenvolvida em **Python** com interface gráfica (GUI) para automatizar a exclusão de arquivos **XML de Notas Fiscais Eletrônicas (NFe)**. A exclusão é realizada com base em uma lista de chaves de NFe fornecidas em uma planilha Excel, otimizando a gestão documental fiscal.

O sistema é particularmente útil para **escritórios contábeis**, **departamentos fiscais** e profissionais que buscam eficiência na organização e manutenção de documentos fiscais digitais.

---

## 📖 Sobre o Projeto

O **PRograma_Excluir_XMLs** simplifica o processo de gerenciamento de XMLs de NFe através das seguintes etapas automatizadas:

1.  **Leitura da Planilha Excel**: O programa inicia lendo uma planilha Excel que contém as chaves das Notas Fiscais Eletrônicas a serem excluídas.
2.  **Seleção de Diretório**: O usuário seleciona a pasta onde os arquivos XML de NFe estão armazenados.
3.  **Comparação e Identificação**: As chaves lidas da planilha são comparadas com os nomes dos arquivos XML presentes na pasta selecionada.
4.  **Exclusão Automatizada**: Os arquivos XML cujas chaves correspondem são automaticamente excluídos do sistema.
5.  **Registro de Atividades**: Todas as ações realizadas, incluindo arquivos identificados e excluídos, são detalhadamente registradas em um arquivo de log para auditoria e acompanhamento.

---

## ✅ Funcionalidades Principais

O programa oferece um conjunto de funcionalidades projetadas para garantir a eficiência e segurança do processo:

*   **Interface Gráfica Intuitiva**: Desenvolvida com **Tkinter**, proporciona uma experiência de usuário simplificada.
*   **Seleção Flexível**: Permite a seleção fácil da planilha Excel de entrada e do diretório contendo os arquivos XML.
*   **Processamento Inteligente**: Realiza a leitura automática das chaves de NFe e a identificação correspondente nos nomes dos arquivos XML.
*   **Exclusão Segura**: Garante a remoção dos arquivos XML de forma controlada e rastreável.
*   **Auditoria Completa**: Gera um arquivo de log (`.txt`) detalhado com todas as operações realizadas.
*   **Portabilidade**: Compatível com a geração de executáveis (`.exe`), permitindo a execução em ambientes Windows sem a necessidade de instalação prévia do Python.

---

## 🧱 Estrutura da Planilha Excel

A planilha de entrada deve seguir um formato específico para que o programa possa processar as informações corretamente. É mandatório que contenha uma coluna nomeada **`CHAVE`**.

### Exemplo de Estrutura da Planilha:

| CHAVE |
| :--------------------------------------- |
| 35240123456789000123550010000000011000000001 |
| 35240123456789000123550010000000021000000002 |

---

## 📁 Estrutura dos Arquivos XML

Os arquivos XML devem ter a chave da NFe incorporada em seu nome para que o sistema possa realizar a correspondência. O programa é capaz de extrair a chave diretamente do nome do arquivo.

### Exemplo de Nome de Arquivo XML:

`NFe35240123456789000123550010000000011000000001.xml`

---

## ⚙️ Requisitos de Desenvolvimento

Para executar o **PRograma_Excluir_XMLs** em modo de desenvolvimento, são necessários os seguintes requisitos:

*   **Python**: Versão 3.10 ou superior.
*   **Sistema Operacional**: Windows.

### Instalação de Dependências:

As bibliotecas Python necessárias podem ser instaladas via `pip`:

```bash
pip install pandas openpyxl
```

---

## ▶️ Como Executar o Programa

Após a instalação das dependências, o programa pode ser executado diretamente via terminal:

```bash
python excluir_xml_nfe.py
```

Siga os passos na interface gráfica:

1.  Clique em **`Selecionar Excel`** e escolha a planilha contendo as chaves.
2.  Clique em **`Selecionar Pasta`** e indique o diretório dos arquivos XML.
3.  Clique em **`INICIAR EXCLUSÃO`** para processar e excluir os arquivos.

---

## 🧾 Arquivo de Log

Um arquivo de log, denominado `log_exclusao.txt`, é gerado automaticamente na mesma pasta do executável, registrando todas as operações de exclusão.

---

## 🖥️ Geração de Executável (.exe)

Para criar um executável independente do Python, utilize a ferramenta `PyInstaller`.

### Instalação do PyInstaller:

```bash
pip install pyinstaller
```

Caso o comando `pyinstaller` não seja reconhecido, utilize:

```bash
python -m PyInstaller --version
```

### Comando para Criar o Executável:

Navegue até a pasta raiz do projeto no terminal e execute o seguinte comando:

```bash
python -m PyInstaller --onefile --windowed --clean --noconfirm --hidden-import=openpyxl excluir_xml_nfe.py
```

O executável será gerado no diretório `dist/excluir_xml_nfe.exe`.

### Adicionando um Ícone ao Executável:

Para personalizar o executável com um ícone (`.ico`), utilize:

```bash
python -m PyInstaller --onefile --windowed --icon=icone.ico excluir_xml_nfe.py
```

---

## ⚠️ Solução de Problemas Comuns

**Problema**: `pyinstaller` não reconhecido.

**Solução**: Utilize o comando completo para invocar o `PyInstaller` via módulo Python:

```bash
python -m PyInstaller
```

---
## ✅ Funcionalidades

- Interface gráfica com **Tkinter**
- Seleção de planilha Excel
- Seleção de pasta dos XMLs
- Leitura automática das chaves NFe
- Exclusão segura dos arquivos XML
- Registro detalhado em log `.txt`
- Compatível com executável `.exe` (sem Python instalado)

---

## 🚀 Melhorias Futuras

As seguintes melhorias estão planejadas para futuras versões do **PRograma_Excluir_XMLs**:

*   **Leitura Direta do XML**: Implementação da capacidade de ler a chave diretamente do conteúdo do arquivo XML, em vez de depender apenas do nome do arquivo.
*   **Barra de Progresso**: Adição de uma barra de progresso na interface gráfica para acompanhar o status da exclusão.
*   **Backup Automático**: Funcionalidade de backup dos arquivos XML antes da exclusão para maior segurança.
*   **Interface Moderna**: Atualização da interface gráfica utilizando bibliotecas como CustomTkinter para um design mais moderno e responsivo.
*   **Cancelamento de Execução**: Opção para interromper o processo de exclusão a qualquer momento.
*   **Instalador Profissional**: Criação de um instalador para facilitar a distribuição e instalação do programa.
*   **Atualizações Automáticas**: Implementação de um sistema de atualização automática para manter o programa sempre na versão mais recente.

---
## link do programa

https://drive.google.com/file/d/1LtZ3yZ_usunegIt9agEtsBwIVBMswJwT/view?usp=sharing

---



