def solution(myString):
    
    myString = myString.replace("x"," ")    
    s_list = list(myString.split())
    s_list.sort()
    return s_list