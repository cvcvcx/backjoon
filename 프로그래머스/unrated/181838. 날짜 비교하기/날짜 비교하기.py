def solution(date1, date2):
    answer = 0
    
    date1_y,date1_m,date1_d = date1
    date2_y,date2_m,date2_d = date2
    
    if date2_y > date1_y:
        answer = 1
    elif date2_y == date1_y:
        if date2_m > date1_m:
            answer = 1
        elif date2_m == date1_m:
            if date2_d >date1_d:
                answer = 1
            else:
                answer = 0
        else:
            answer = 0
    else:
        answer = 0
    
    
    return answer