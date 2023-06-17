def solution(my_string, s, e):
    answer = ''
    sliced_string = my_string[s:e+1]
    reversed_sliced_string = sliced_string[::-1]
    answer = my_string[:s]+reversed_sliced_string+my_string[e+1:]
    return answer