def solution(s, skip, index):
    al = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for c in skip:
        al = al.replace(c,"")
        
    for c in s:
        ch = al[(al.index(c)+index)%len(al)]
        answer += ch
    return answer