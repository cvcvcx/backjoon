import sys

input = sys.stdin.readline
n = int(input().strip())
s_list = []
for _ in range(n):
    s_list.append(input().strip())
s_set = set(s_list)
s_set_list = list(s_set)
s_set_list.sort()
s_set_list.sort(key=len)

for s in s_set_list:
    print(s)
