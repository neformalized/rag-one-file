from rag import RAG

with open("C:\\Users\\omni\\Desktop\\document.txt", "r", encoding = "utf-8") as f:
    
    doc = f.read()
    
    store = RAG(doc)
#

print(store.query("Очікування від ШІ", top_k = 3, enhance = 5))