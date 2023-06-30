import sys
input = sys.stdin.readline

n = int(input())
my_card_list = {num:1 for num in list(map(int,input().split()))}
m = int(input())
find_number_list = list(map(int,input().split()))
for num in find_number_list:
    if num in my_card_list:
        print(1,end=" ")
    else:
        print(0,end=" ")
        