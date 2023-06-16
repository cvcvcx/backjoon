def solution(my_string):
    answer = ''
    al_list = ["a","e","i","o","u"]
    for al in al_list:
        my_string = my_string.replace(al,"")
    answer = my_string
    return answer