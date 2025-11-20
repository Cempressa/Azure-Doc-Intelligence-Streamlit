-----

## ✅ Versão Final Sugerida do README

```markdown
# Azure-Doc-Intelligence-Streamlit

Streamlit + Azure Document Intelligence para upload e análise de documentos.

## 📄 Descrição
Este projeto é uma aplicação web desenvolvida em **Streamlit** como parte do desafio [**Nome do Desafio DIO, se aplicável**], com o objetivo de simular a extração e validação de informações de documentos (como cartões de crédito) utilizando o serviço **Azure AI Document Intelligence**.

A aplicação permite o upload de arquivos PDF ou imagem, gerencia o armazenamento via **Azure Blob Storage** e demonstra a modularização de um projeto Python.

## 🛠️ Estrutura do Projeto e Tecnologias
* **Interface:** Streamlit
* **Cloud:** Azure Blob Storage (Simulação de Upload/Download)
* **Linguagem:** Python 3.x
* **Modularização:** Uso das pastas `src/utils` e `src/services` para organização de código.
* **Dependências:** `requirements.txt`

---

## 🚀 Como Executar Localmente

Siga os passos abaixo na pasta raiz (`Docs`) do projeto:

1.  Clone o repositório.
2.  Crie um ambiente virtual: `python -m venv .venv`
3.  Ative o ambiente: `.\.venv\Scripts\Activate` (Windows PowerShell)
4.  Instale todas as dependências: `pip install -r requirements.txt`
5.  **Configuração:** Crie o arquivo `.env` na raiz do projeto e insira suas credenciais do Azure (`ENDPOINT`, `KEY`, `AZURE_STORAGE_CONNECTION_STRING`, etc.).
6.  **Execute a aplicação (do diretório raiz):** `streamlit run src/app.py`

---

## 📁 Estrutura de Diretórios
```

.
├── .venv/ (Ignorado pelo Git)
├── .env (Ignorado pelo Git)
├── src/
│   ├── app.py (Ponto de entrada do Streamlit)
│   ├── services/
│   │   └── blob\_service.py (Lógica de upload para Azure)
│   └── utils/
│       └── Config.py (Carregamento de variáveis de ambiente)
└── requirements.txt

---
**Recomendação:** Se você não criou o arquivo `requirements.txt` com o `pip freeze`, certifique-se de que ele contenha pelo menos: `streamlit`, `azure-storage-blob`, e `python-dotenv`.
---
