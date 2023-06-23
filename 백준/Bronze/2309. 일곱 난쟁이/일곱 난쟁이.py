import sys
input = sys.stdin.readline

num_list = [int(input().strip()) for _ in range(9)]
one = 0
two = 0
sum_ = sum(num_list)
for i in range(len(num_list)-1):
    for j in range(i+1,len(num_list)):
        if sum_ - (num_list[i]+num_list[j]) == 100:
            one = num_list[i]
            two = num_list[j]
            break
            
            
num_list.remove(one)
num_list.remove(two)
num_list.sort()

for s in num_list:
    print(s)
