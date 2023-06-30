import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

A_minus_B = A-B
B_minus_A = B-A
answer = A_minus_B | B_minus_A
print(len(answer))