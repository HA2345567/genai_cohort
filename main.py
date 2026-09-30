from pathlib import Path
import os

from dotenv import load_dotenv


project_root = Path(__file__).resolve().parent
local_temp = project_root / ".tmp"
local_temp.mkdir(exist_ok=True)
os.environ["TEMP"] = str(local_temp)
os.environ["TMP"] = str(local_temp)
os.environ["HF_HOME"] = str(local_temp / "huggingface")

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import TokenTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings


load_dotenv()


pdf_path = project_root / "documents_loaders" / "notes.pdf"

loader = PyPDFLoader(str(pdf_path))

data = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = splitter.split_documents(data)

print(f"Created {len(chunks)} chunks.")


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vectorStore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=str(project_root / "chroma_huggingface_db"),
    collection_name="notes_huggingface"
)

print("Documents successfully stored in Chroma!")