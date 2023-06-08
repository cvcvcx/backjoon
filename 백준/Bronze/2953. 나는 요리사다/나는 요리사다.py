human=[list(map(int,input().split())) for _ in range(5)]
human_score = [0]*5
score = 0
for i in range(5):
    sum = 0
    for j in range(4):
        sum += human[i][j]
    human_score[i] = sum
    score = max(score, human_score[i])
for i in range(5):
    if score == human_score[i]:
        print(i+1,score)
        break
    