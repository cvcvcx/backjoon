def solution(babbling):
    answer = 0
    can_say = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for w in can_say:
            if w*2 not in b:
                b = b.replace(w,' ')
        if len(b.strip())==0:
            answer += 1
    
    return answer