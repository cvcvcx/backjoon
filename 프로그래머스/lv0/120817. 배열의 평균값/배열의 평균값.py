def solution(numbers):
    answer = 0
    sum_number = 0
    for number in numbers:
        sum_number += number
    
    answer = (format((sum_number/len(numbers)),".1f"))
    
    return answer