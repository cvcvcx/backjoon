def solution(numbers):
    answer = 0
    for num in numbers:
        answer += num
    answer = format(answer/len(numbers),".1f")
    return answer