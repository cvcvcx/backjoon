def solution(myString):
    answer = []
    s_list = myString.split("x")
    answer = [len(s) for s in s_list]
    return answer