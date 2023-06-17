def solution(s):
    answer = ''
    word_list = s.split(" ")
    print(word_list)
    for word in word_list:
        for i,w in enumerate(word):
            if i % 2 == 0 :
                answer += w.upper()
            else:
                answer += w.lower()
        answer += " "
    answer = answer[:-1]
    return answer