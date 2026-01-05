def dedup(bundle_of_chunks: list[list[dict]]) -> list[str]:
    
    seen = list()
    results = list()
    
    #
    
    for chunks in bundle_of_chunks:
        
        for chunk in chunks:
            
            if chunk["idx"] not in seen:
                
                results.append(chunk["text"])
                seen.append(chunk["idx"])
            #
        #
    #
    
    return results
#