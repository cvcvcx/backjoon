def solution(absolutes, signs):
    num_list = []
    for i, num in enumerate(absolutes):
        if signs[i] == False:
            num_list.append(num * -1)
        else:
            num_list.append(num)
    return sum(num_list)