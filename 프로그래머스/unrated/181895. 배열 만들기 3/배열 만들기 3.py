def solution(arr, intervals):
    answer = []
    a1,b1 = intervals[0]
    a2,b2 = intervals[1]
    sliced_arr_1 = arr[a1:b1+1]
    sliced_arr_2 = arr[a2:b2+1]
    answer = sliced_arr_1 + sliced_arr_2
    return answer