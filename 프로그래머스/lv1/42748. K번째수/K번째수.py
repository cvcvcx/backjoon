def solution(array, commands):
    answer = []
    for c in commands:
        c_array = array[c[0]-1:c[1]]
        c_array.sort()
        answer.append(c_array[(c[2]-1)])
    return answer