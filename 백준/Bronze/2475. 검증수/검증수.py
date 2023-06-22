num_list = map(int,input().split())
num_multiply_num_list = [n**2 for n in num_list]
sum_mul_nums = sum(num_multiply_num_list)
print(sum_mul_nums%10)
