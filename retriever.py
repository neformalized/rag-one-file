def dedup(bundle_of_chunks: list[list[dict]]) -> list[dict]:
    
    results, results_sorted = dict(), dict()
    
    #
    
    for chunks in bundle_of_chunks:
        
        for chunk in chunks:
            
            if chunk["idx"] not in results.keys():
                
                results[chunk["idx"]] = chunk["text"]
            #
        #
    #
    
    for key in sorted(results):
        
        results_sorted[key] = results[key]
    #
    
    return results_sorted
#