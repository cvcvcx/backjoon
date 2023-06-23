import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
abs_num_dict = {}
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum_numbers = num_list[i] + num_list[j] + num_list[k]
            if sum_numbers <= m:
                abs_num_dict[abs(sum_numbers - m)] = sum_numbers
sorted_abs_keys = sorted(list(abs_num_dict.keys()))
print(abs_num_dict[sorted_abs_keys[0]])