while True:
    n = int(input())
    if n == -1:
        break
    num_list = []
    for num in range(1,n):
        if n%num ==0:
            num_list.append(num)
    answer = ""
    if sum(num_list) == n:
        answer = f"{n} = "
        for l in num_list:
            answer += str(l) + " + "
        print(answer[:-3])
    else:
        print(f"{n} is NOT perfect.")