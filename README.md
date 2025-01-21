# Dúvidas Lucas Tech - FAQ Virtual com RAG

Este projeto utiliza a técnica de **Retrieval-Augmented Generation (RAG)** para criar um assistente virtual que responde dúvidas relacionadas à empresa fictícia *Lucas Tech*. O sistema utiliza **Streamlit** para a interface de usuário e as bibliotecas **LangChain** e **Google Generative AI** para o processamento de linguagem natural e recuperação de informações.

## Recursos Principais

- **Streamlit**: Interface simples e interativa para interagir com o assistente.
- **LangChain**: Utilizado para criar a pipeline de geração de respostas e recuperação de informações.
- **Google Generative AI**: Para embeddings de alta qualidade e geração de texto.
- **FAISS**: Indexação eficiente para busca de similaridade nos documentos carregados.

## Requisitos

Antes de começar, certifique-se de ter as seguintes dependências instaladas:

- Python 3.9+
- Streamlit
- langchain_community
- langchain_google_genai
- python-dotenv
- FAISS

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/lucasmarcolino-dev/chatbot-langchain
   ```
   
2. Crie um arquivo `.env` na raiz do projeto com as credenciais necessárias:

   ```env
   GOOGLE_API_KEY=<sua_chave_api_google>
   ```

3. Certifique-se de que o arquivo `lucas_tech_faq.csv` está presente no diretório raiz do projeto. Este arquivo deve conter os documentos a serem utilizados pelo sistema.

## Uso

1. Inicie o servidor Streamlit:

   ```bash
   streamlit run main.py
   ```

2. Acesse a aplicação no navegador pelo endereço exibido no terminal (geralmente `http://localhost:8501`).

3. Digite sua pergunta no campo de texto e obtenha respostas claras e objetivas relacionadas à Lucas Tech.

## Estrutura do Código

- **`CSVLoader`**: Carrega os dados do arquivo CSV para documentos utilizáveis.
- **`GoogleGenerativeAIEmbeddings`**: Gera embeddings dos documentos para busca de similaridade.
- **`FAISS`**: Cria um banco de dados para busca eficiente.
- **`PromptTemplate`**: Define o modelo de prompt usado para geração de respostas.
- **`ChatGoogleGenerativeAI`**: Responsável por gerar respostas baseadas no prompt e no modelo de linguagem da Google.

## Fluxo do Sistema

1. **Carregamento de Documentos**: Os dados são carregados do arquivo `lucas_tech_faq.csv`.
2. **Indexação com FAISS**: Os documentos são indexados usando embeddings gerados pelo modelo `GoogleGenerativeAIEmbeddings`.
3. **Consulta**: A consulta do usuário é processada, e os documentos mais relevantes são recuperados.
4. **Geração de Resposta**: O conteúdo do documento recuperado é utilizado para compor uma resposta clara e direta.
