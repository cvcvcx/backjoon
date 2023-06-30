import sys
input = sys.stdin.readline
n, m = map(int,input().split())
pocket_idx_dict = {}
idx_pocket_dict = {}
for i in range(1,n+1):
    pocket = input().strip()
    pocket_idx_dict[pocket] = i
    idx_pocket_dict[i] = pocket
for _ in range(m):
    s = input().strip()
    if s.isdigit():
        print(idx_pocket_dict[int(s)])
    else:
        print(pocket_idx_dict[s])