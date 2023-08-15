from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
#from langchain.document_loaders import UnstructuredWordDocumentLoader # use case for word
#from langchain.document_loaders import UnstructuredCSVLoader  # use case for CSV
#from langchain.document_loaders import UnstructuredPowerPointLoader  # use case for ppt
from langchain.embeddings import  HuggingFaceEmbeddings # get HF embeddings or use sentnece transformers
from langchain.vectorstores import FAISS # Facebook similarity search... or something like that

DATA_PATH = "data/"    # data path
DB_FAISS_PATH = "vectorstores/db_faiss"  # embedding path

# Create vector database

def create_vector_db():
    loader = DirectoryLoader(DATA_PATH,glob='*.pdf',loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size= 500, chunk_overlap= 50)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2', model_kwargs = {'device':'cpu'}) # interchange with GPU if available

    db = FAISS.from_documents(texts , embeddings) # creating the vector database providing the texts and the embeddings.
    db.save_local(DB_FAISS_PATH) # saved at FAISS path


if __name__ == '__main__':
    create_vector_db()