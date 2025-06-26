import os
import logging
import ollama
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers import MultiQueryRetriever
from langchain.chains import ConversationalRetrievalChain


#configuring logging
logging.basicConfig(level=logging.INFO)

#CONSTANTS
DOC_PATH = "./data/technique.pdf"
MODEL_NAME = "carlos:latest"
EMBEDDING_MODEL = "nomic-embed-text:latest"
VECTOR_STORE_NAME = "carlos_assistant"


#ingesting and loading our pdf:
def ingest_pdf(doc_path):
    """Load PDF Document"""
    if os.path.exists(doc_path):
        loader = UnstructuredPDFLoader(file_path=doc_path)
        data= loader.load()
        logging.info("PDF loaded successfully! I am almost ready carino, just wait a sec.")
        return data
    
    else:
        logging.error(f"Did you forget to upload the file mi carino? : {doc_path}")
        return None



#splitting and chunking of the pdf document
def split_document(documents):
    """Well I gotta split the documents into smaller chunks for you mi vida..."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1200, chunk_overlap = 300)
    chunks = text_splitter.split_documents(documents)
    logging.info(f"I have split the documents for us, mi vida")
    return chunks


def create_vectordb(chunks):
    """Creating a vector database from document chunks"""
    #pull the model if not present
    ollama.pull(EMBEDDING_MODEL)
    vector_db= Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model=EMBEDDING_MODEL),
        collection_name=VECTOR_STORE_NAME)
    logging.info(f"My vector database is finally created, mi precioso loco!")
    return vector_db


#creating a retriever - here we put prompts, llm, retrievers
def create_retriever(vector_db, llm):
    """Creating multiqueries retriever for document"""
    #setting a model to use
    llm = ChatOllama(model=MODEL_NAME)
    QUERY_PROMPT= PromptTemplate(
        input_variables=["question"],
        template="""Carlos, here I need your help as an AI language model assistant. Your task
                    is to help generate five different versions of the given user question to
                    retrieve relevant documents from a vector database. By generating multiple
                    perspectives on the user question, your goal is to help the user overcome the
                    limitations of the distance-based similarity search. Provide these alternative
                    questioms separated by newlinnes.
                    Original question : {question}"""
    )


    retriever = MultiQueryRetriever.from_llm(
        vector_db.as_retriever(), llm, prompt=QUERY_PROMPT)
    logging.info(f"Retriever created.")
    return retriever

     

def create_chain(retriever, llm):
    """Creating the chain for processing input and giving output"""
    #RAG PROMPT
    template="""Answer the question ONLY based on the following context : 
    {context}
    Question : {question}
    """


    answer_prompt=ChatPromptTemplate.from_template(template)

    chain= (
        {"context" : retriever, "question" : RunnablePassthrough()}
        | answer_prompt
        | llm
        | StrOutputParser()
    )

    logging.info("Chain created successfully")
    return chain
    


def main():
    #loading the pdf document
    data= ingest_pdf(DOC_PATH)
    if data is None:
        return
    
    #split documents into chunks
    chunks= split_document(data)

    #create vector database
    vector_db=create_vectordb(chunks)

    #initialising the language model
    llm=ChatOllama(model=MODEL_NAME)

    #create the retriever
    retriever = create_retriever(vector_db, llm)

    #creating the chain
    chain= create_chain(retriever, llm)

    #query input
    question = "What is Floor fences and why do we need them?"

    #get the response
    response= chain.invoke(input=question)
    print("Okay, so what you are asking for is :", response)

if __name__=="__main__":
    main()