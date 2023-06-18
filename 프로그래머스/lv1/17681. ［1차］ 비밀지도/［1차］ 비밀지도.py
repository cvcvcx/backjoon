def solution(n, arr1, arr2):
    answer = [""]*n
    bin_arr1 = []
    bin_arr2 = []
    for num in arr1:
        bin_ = ""
        while num>0:
            bin_ += str(num%2)
            num = num//2
        while len(bin_)<n:
            bin_ += "0"
        bin_arr1.append(bin_[::-1])
        
    for num in arr2:
        bin_ = ""
        while num>0:
            bin_ += str(num%2)
            num = num//2
        while len(bin_)<n:
            bin_ += "0"
        bin_arr2.append(bin_[::-1])

        
    for i in range(n):
        for j in range(n):
            if max(int(bin_arr1[i][j]),int(bin_arr2[i][j])) == 1:
                answer[i] += "#"
            else:
                answer[i] += " "
    return answer