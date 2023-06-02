def solution(n, k):
    answer = 0
    meat = 12000
    drink = 2000
    service = 0
    if(n>=10):
        service = (n//10) * drink
    answer = n*meat + k*drink - service
    
    return answer