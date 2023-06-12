def solution(babbling):
    answer = 0
    say_word_list = ["aya","ye","woo","ma"]
    for word in babbling:
        for say_word in say_word_list:
            word = word.replace(say_word,"!",1)
        if word.replace("!",'') == '':
            answer += 1
    return answer