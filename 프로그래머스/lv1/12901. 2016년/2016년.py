def solution(a, b):
    answer = ''
    #1,3,5,7,8,10,12 => 31일
    #4,6,9,11 => 30일
    #2 => 29일
    cal_dict = {}
    
    day_dict = {0:"THU",1:"FRI",2:"SAT",3:"SUN",4:"MON",5:"TUE",6:"WED"}
    for i in range(1,12+1):
        if i == 2:
            cal_dict[i] = 29
        elif i == 4 or i == 6 or i == 9 or i == 11:
            cal_dict[i] = 30
        else:
            cal_dict[i] = 31
    today_to_date = b
    for m in range(1,a):
        today_to_date += cal_dict[m]
    
    answer = day_dict[today_to_date%7]
    return answer