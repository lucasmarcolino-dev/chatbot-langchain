import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import CSVLoader
from dotenv import load_dotenv

load_dotenv()

loader = CSVLoader(file_path="lucas_tech_faq.csv")
documents = loader.load()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
db = FAISS.from_documents(documents, embeddings)

def retrieve_info(query):
    similar_response = db.similarity_search(query, k=3)
    return [doc for doc in similar_response]


llm = ChatGoogleGenerativeAI(temperature=0.3, model="gemini-1.5-pro")

template = """Você é um assistente virtual para uma empresa de tecnologia chamada Luca's Tech.
Seja o mais claro possível:

{question}
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=template
)

pipeline = prompt | llm


def generate_response(message):
    retrieved_info = retrieve_info(message)
    if not retrieved_info:
        return "Não foi possível encontrar informações relacionadas à sua consulta."

    content = retrieved_info[0].content if hasattr(retrieved_info[0], "content") else retrieved_info[0].page_content

    answer = content.split("Answer:", 1)[1].strip()
    return answer

def main():
    st.set_page_config(page_title="Dúvidas Lucas Tech", page_icon=":bird")

    st.header("Pergunte Sobre a empresa")
    message = st.text_area("Pergunta")

    if message:
        st.write("Escrevendo resposta...")

        result = generate_response(message)

        st.info(result)

        st.empty()

if __name__ == '__main__':
    main()