def solution(score):
    answer = []
    li = []
    
    for a,b in score:
        li.append((a+b)/2)
        
    sorted_arr = sorted(li,reverse = True)
    for i in li:
        answer.append(sorted_arr.index(i)+1)
    
    return answer