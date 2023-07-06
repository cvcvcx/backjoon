n = int(input())
num_list = list(map(int,input().split()))

num_list.sort()
count = 0
for k in range(n):
    find = num_list[k]
    i = 0
    j = n - 1
    
    while i<j:
        if num_list[i] + num_list[j] == find:
            if i != k and j != k: 
                count +=1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif num_list[i] + num_list[j] < find:
            i += 1
        elif num_list[i] + num_list[j] > find:
            j -= 1
print(count)