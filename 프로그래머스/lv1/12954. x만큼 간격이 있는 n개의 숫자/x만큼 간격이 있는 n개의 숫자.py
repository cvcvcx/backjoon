def solution(x, n):
    answer = []
    input_number = 0
    for _ in range(n):
        input_number += x
        answer.append(input_number)
    return answer