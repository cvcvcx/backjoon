def solution(d, budget):
    answer = 0
    d.sort()
    for price in d:
        if budget - price >= 0:
            answer += 1
            budget -= price
    return answer