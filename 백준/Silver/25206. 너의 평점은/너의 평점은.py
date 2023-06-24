n = 20
score_dict = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
sub_count = 0
sum_score = 0
for _ in range(n):
    subject, g, score = input().split()
    if score == "P":
        continue
    else:
        sub_count += float(g)
        sum_score += float(g) * score_dict[score]
print(sum_score/sub_count)