n =  int(input())

answer = 0

for _ in range(n):
    word = input()
    not_group_word = False
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if word[i] in new_word:
                not_group_word = True
                break
    if not_group_word == False:
        answer += 1
print(answer)