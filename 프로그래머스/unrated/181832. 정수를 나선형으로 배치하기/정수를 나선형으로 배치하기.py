def solution(n):
    #이번에 들어갈 숫자
    input_number = 0
    #배열 선언
    arr = [[0]*n for _ in range(n)]
    #증감 횟수 (첫번째 줄을 기준으로 증감)
    k = n
    #좌표의 맨 처음 값(0,-1)에서 맨 처음에만 5회 반복을 해야하는데, 좌표값의 변동을 안에서 따로 조건문으로 하기보다, 0,-1로 시작하게끔 함
    i, j = 0, -1
    #증감 값 방향에 따라서 +1 또는 -1
    s = 1

    
    while input_number < n*n:
        while j+s<n and arr[i][j+s] == 0 :
            input_number += 1 # 1 
            j += s # 0 
            arr[i][j] = input_number # arr[0][0] = 1

        k = k - 1
        if k<0:
            break
            
        while i+s<n and arr[i+s][j] == 0 :
            input_number += 1
            i += s
            arr[i][j] = input_number
        s *= -1
    
    return arr