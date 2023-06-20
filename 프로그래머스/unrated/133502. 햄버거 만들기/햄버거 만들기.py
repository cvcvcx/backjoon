def solution(ingredient):
    answer = 0
    ham = []
    for s in ingredient:
        ham.append(s)
        if ham[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                ham.pop()
    return answer