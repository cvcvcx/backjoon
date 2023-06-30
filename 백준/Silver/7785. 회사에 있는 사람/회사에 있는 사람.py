import sys
input = sys.stdin.readline
n = int(input())
people_dict = {}

for _ in range(n):
    people,state = input().split()
    if state == "enter":
        people_dict[people] = 1
    else:
        state == "leave"
        if people in people_dict:
            del people_dict[people]
people_list = list(people_dict.keys())
people_list.sort(reverse = True)
for key in people_list:
    print(key)