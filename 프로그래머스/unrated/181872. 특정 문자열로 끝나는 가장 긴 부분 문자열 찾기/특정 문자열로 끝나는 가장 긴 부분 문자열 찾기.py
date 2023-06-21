def solution(myString, pat):
    reverse_s = myString[::-1]
    reverse_p = pat[::-1]
    return myString[:len(myString) - reverse_s.index(reverse_p)]