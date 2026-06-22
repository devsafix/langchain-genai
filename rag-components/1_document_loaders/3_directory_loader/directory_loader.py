from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

loader = DirectoryLoader(
    path=str(BASE_DIR / 'books'),
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)