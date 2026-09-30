import sys
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator = "\n\n",
    chunk_size = 10,
    chunk_overlap = 1
)
# Ensure UTF-8 output encoding for Windows console
sys.stdout.reconfigure(encoding="utf-8")

file_path = Path(__file__).parent / "notes.txt"
data = TextLoader(str(file_path)).load()

print(f"Loaded {len(data)} pages.\n")

doc_chunk = splitter.split_documents(data)

