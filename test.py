from engine import rag

with open("C:\\Users\\omni\\Desktop\\document.txt", "r", encoding = "utf-8") as f:
    
    doc = f.read()
    
    store = rag.RAG(doc)
#

print(store.query("Ожидания от искуственного интеллекта", top_k = 3, enhance = 5))