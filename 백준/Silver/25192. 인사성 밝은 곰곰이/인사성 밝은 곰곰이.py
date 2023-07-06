n = int(input())
chat_list = set()
answer = 0
for _ in range(n):
    s = input()
    if s == "ENTER":
        answer += len(chat_list)
        chat_list.clear()
    elif s not in chat_list:
        chat_list.add(s)
answer += len(chat_list)

print(answer)