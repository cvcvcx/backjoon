alpha = "abcdefghijklmnopqrstuvwxyz"
al_count_list = []
s = input()

for al in alpha:
    if al in s:
        al_count_list.append(s.index(al))
    else:
        al_count_list.append(-1)
answer = ""
for count in al_count_list:
    answer += str(count) + " "
print(answer[:-1])
