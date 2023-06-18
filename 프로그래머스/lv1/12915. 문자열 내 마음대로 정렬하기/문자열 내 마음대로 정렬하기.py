def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    
    strings.sort()
    
    for s in strings:
        answer.append(s[1:])
    
    return answer