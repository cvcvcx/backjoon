def solution(strArr):
    answer = 0
    len_arr = [len(s) for s in strArr]
    len_arr.sort()
    count_arr = {}
    for l in range(0,len(len_arr)):
        if len_arr[l-1] == len_arr[l] :
            if count_arr and count_arr[len_arr[l]]:
                count_arr[len_arr[l]] += 1
            else:
                count_arr[len_arr[l]] = 1    
        else:
            count_arr[len_arr[l]] = 1
    return max(list(count_arr.values()))