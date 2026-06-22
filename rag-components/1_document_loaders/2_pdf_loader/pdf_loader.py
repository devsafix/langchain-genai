from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

loader = PyPDFLoader(str(BASE_DIR / 'taqwasoftware.pdf'))

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)