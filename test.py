from handler import RAG
import asyncio

with open("C:\\Users\\omni\\Desktop\\document.txt", "r", encoding = "utf-8") as file:
    
    ragged_doc = RAG(file.read())
#

print(ragged_doc.query("Ожидания от внедрения ии", top_k = 3, enhance = 5))