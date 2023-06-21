def solution(array, n):
    minus_dic = {}
    
    for num in array:
        
        if abs(num-n) in minus_dic:
            minus_dic[abs(num-n)].append(num)
        else:
            minus_dic[abs(num-n)] = [num]
        
    return min(minus_dic[min(list(minus_dic.keys()))])