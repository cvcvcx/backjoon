def solution(myStr):
    myStr = myStr.replace("a"," ")
    myStr = myStr.replace("b"," ")
    myStr = myStr.replace("c"," ")
    
    answer = list(myStr.split())
    
    return answer or ["EMPTY"]