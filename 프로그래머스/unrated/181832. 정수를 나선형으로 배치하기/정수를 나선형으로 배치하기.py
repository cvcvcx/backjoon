def solution(n):
    input_number = 0
    answer = [[0]*n for _ in range(n)]
    k = n
    i, j = 0, -1
    s = 1
    while input_number<n**2:
        for _ in range(k):
            input_number += 1
            j += s
            answer[i][j] = input_number
        
        k -= 1
        if(k<0):
            break
            
        for _ in range(k):
            input_number += 1
            i += s
            answer[i][j] = input_number
            
        s *= -1
        
    return answer