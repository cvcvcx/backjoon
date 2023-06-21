def solution(arr):
    answer = 0
    prev_arr = []
    while prev_arr != arr:
        answer += 1
        prev_arr = arr[:len(arr)]
        for i,n in enumerate(arr):
            if n >= 50 and n%2==0:
                arr[i] = int(n/2)
            elif n<50 and n%2 == 1:
                arr[i] = n*2+1

    return answer-1