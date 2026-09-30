
# Load the PDF, split it into chunks, create embeddings, and store them in Chroma.
import os
from pathlib import Path


project_root = Path(__file__).resolve().parent
local_temp = project_root / ".tmp"
local_temp.mkdir(exist_ok=True)
os.environ["TEMP"] = str(local_temp)
os.environ["TMP"] = str(local_temp)
os.environ["HF_HOME"] = str(local_temp / "huggingface")


from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv(project_root / ".env")

pdf_path = project_root / "documents_loaders" / "notes.pdf"
chroma_path = project_root / "chroma_huggingface_db"
chroma_path.mkdir(exist_ok=True)

loader = PyPDFLoader(str(pdf_path))

data = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
chunks = splitter.split_documents(data)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorStore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=str(chroma_path),
    collection_name="notes_huggingface"
)

print(f"Stored {len(chunks)} document chunks in Chroma.")


