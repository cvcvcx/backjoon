def solution(order):
    answer =0
    str_order = str(order)
    for s in str_order:
        if s == "3" or s == "6" or s == "9":
            answer += 1
    return answer