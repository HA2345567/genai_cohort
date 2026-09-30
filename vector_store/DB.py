import os
from pathlib import Path


project_root = Path(__file__).resolve().parents[1]
local_temp = project_root / ".tmp"
local_temp.mkdir(exist_ok=True)
os.environ["TEMP"] = str(local_temp)
os.environ["TMP"] = str(local_temp)
os.environ["HF_HOME"] = str(local_temp / "huggingface")

from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

docs = [
    Document(
        page_content=(
            "Python is a high-level, interpreted programming language "
            "widely used in Artificial Intelligence, Machine Learning, "
            "data science, automation, and web development."
        ),
        metadata={
            "source": "ai_basics.txt",
            "topic": "Artificial Intelligence",
            "category": "programming",
            "language": "Python",
            "document_id": "doc_001"
        }
    ),
]

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorStore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory=str(project_root / "chroma_huggingface_db"),
    collection_name="ai_basics_huggingface"
)

result = vectorStore.similarity_search("What is Python used for in AI?", k=2)

for r in result:
    print(r.page_content)
    
retriver = vectorStore.as_retriever()

docs = retriver.invoke("What is Python used for in AI?")  

for d in docs:
    print(d.page_content)