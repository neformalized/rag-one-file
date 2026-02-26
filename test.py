from rag import RAG

with open("path_to_file.txt", "r", encoding = "utf-8") as f:
    
    doc = f.read()
    
    store = RAG(doc)
#

print(store.query("Expectation from AI", top_k = 3, enhance = 5))