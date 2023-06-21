def solution(arr, k):
    list_ = []
    
    for n in arr:
        if n not in list_:
            list_.append(n)
    
    if len(list_)>k:
        list_ = list_[:k]
        
    elif len(list_)<k:
        for i in range(k-len(list_)):
            list_.append(-1)
    
    
    return list_