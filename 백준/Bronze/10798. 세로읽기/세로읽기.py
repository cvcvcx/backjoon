word_list = [input() for _ in range(5)]
for j in range(15):
    for i in range(5):
        if len(word_list[i])>j:
            print(word_list[i][j],end = "")