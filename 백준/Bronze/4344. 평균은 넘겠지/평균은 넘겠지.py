
c = int(input())
for _ in range(c):
    score_list = list(map(int,input().split()))
    n = score_list[0]
    score_list.remove(n)
    sum_score = sum(score_list)
    aver = sum_score/n
    aver_plus_student = 0
    for score in score_list:
        if score > aver:
            aver_plus_student += 1
    answer = aver_plus_student/n * 100
    print(f"{answer:.3f}%")