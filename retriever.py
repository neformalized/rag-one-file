def dedup(bundle_of_chunks: list[list[dict]]) -> list[str]:
    
    results = dict()
    
    #
    
    for chunks in bundle_of_chunks:
        
        for chunk in chunks:
            
            if chunk["idx"] not in results.keys():
                
                results[chunk["idx"]] = chunk["text"]
            #
        #
    #
    
    return [results[idx] for idx in sorted(results.keys())]
#