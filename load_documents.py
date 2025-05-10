from dotenv import load_dotenv
load_dotenv()
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
import os

# Folder containing your split section files
section_folder = "sections_from_pdf2"

# Force UTF-8 decoding to prevent cp1252 errors
loader = DirectoryLoader(
    section_folder,
    glob="*.txt",
    loader_cls=lambda path: TextLoader(path, encoding="utf-8")
)

# Load, embed, and save
docs = loader.load()
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embedding)
vectorstore.save_local("wildlaw_vectorstore")

print("✅ Vector store created and saved!")
