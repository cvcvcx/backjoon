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
      #공백 문자열이 끝날 때, 공백 추가
        answer += " "
    answer = answer[:-1]
    return answer