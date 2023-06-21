def solution(arr, delete_list):
    for del_num in delete_list:
        if del_num in arr:
            arr = [num for num in arr if num != del_num]
    
    return arr