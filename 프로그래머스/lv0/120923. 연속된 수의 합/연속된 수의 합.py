def solution(num, total):
    answer = []
    if num % 2 == 0:
        answer = list(range((total // num) - (num // 2)+1,(total//num)+(num // 2) + 1))
    else:
        answer = list(range((total // num) - (num // 2),(total//num)+(num // 2) + 1))
    return answer