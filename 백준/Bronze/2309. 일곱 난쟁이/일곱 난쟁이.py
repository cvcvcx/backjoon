import sys
input = sys.stdin.readline

num_list = [int(input().strip()) for _ in range(9)]

sum_ = sum(num_list)
answer = [n for n in num_list]
for i in range(len(num_list)-1):
    for j in range(i+1,len(num_list)):
        if sum_ - (num_list[i]+num_list[j]) == 100:
            answer.remove(num_list[i])
            answer.remove(num_list[j])
            answer.sort()
            str_num_list = [str(num) for num in answer]
            for s in str_num_list:
                print(s)
            exit()
