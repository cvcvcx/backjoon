def solution(answers):
    answer = []
    count_answer = [0]*3
    
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            count_answer[0] += 1
        if answers[i] == b[i%8]:
            count_answer[1] += 1
        if answers[i] == c[i%10]:
            count_answer[2] += 1
    for i,c in enumerate(count_answer):
        if max(count_answer) == c:
            answer.append(i+1)
#         if max(count_answer) == c:
#             answer.append(i+1)
    return answer