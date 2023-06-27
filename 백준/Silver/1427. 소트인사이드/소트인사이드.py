n = input()
num_list = list(n)
num_list.sort(reverse=True)
for num in num_list:
    print(num,end="")