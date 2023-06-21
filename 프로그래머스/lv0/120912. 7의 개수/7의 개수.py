def solution(array):
    answer = 0
    for num in array:
        if "7" in str(num):
            answer += str(num).count("7")
    return answer