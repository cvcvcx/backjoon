import sys

input = sys.stdin.readline

n = int(input())
num_count_list = [0] * 10001

for _ in range(n):
    num = int(input())
    num_count_list[num] += 1

for i, num in enumerate(num_count_list):
    if num > 0:
        for _ in range(num):
            print(i)