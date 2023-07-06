n = int(input())
m = int(input())

num_list = list(map(int,input().split()))

num_list.sort()
i = 0
j = len(num_list) - 1
count = 0
while i < j:
    if num_list[i] + num_list[j] == m:
        count += 1
        i += 1
        j -= 1
        
    elif num_list[i] + num_list[j] < m:
        i += 1
        
    elif num_list[i] + num_list[j] > m:
        j -= 1
print(count)