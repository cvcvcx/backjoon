def solution(my_string, is_prefix):
    answer = 0
    start_words = []
    for i in range(1,len(my_string)):
        start_words.append(my_string[:i])
    if is_prefix in start_words:
        answer = 1
    return answer