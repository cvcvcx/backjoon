s_list = []
len_list = []
for _ in range(5):
    word = input()
    s_list.append(word)
    len_list.append(len(word))
    
answer = ''
for i in range(max(len_list)):
    for j in range(5):
        if i < len_list[j]:
            answer += s_list[j][i]
print(answer)