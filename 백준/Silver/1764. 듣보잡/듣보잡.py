import sys
input = sys.stdin.readline

answer_list = []
n, m = map(int,input().split())
no_heard_dict = {input().strip():0 for _ in range(n)}
no_see_dict = {input().strip():0 for _ in range(m)}
for key,value in no_see_dict.items():
    if key in no_heard_dict:
        answer_list.append(key)
        
answer_list.sort()

print(len(answer_list))
for answer in answer_list:
    print(answer)