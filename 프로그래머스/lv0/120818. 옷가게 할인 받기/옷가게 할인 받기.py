def solution(price):
    sale_percent = 0
    if(price>=500000):
        sale_percent = 20
    elif(price>=300000):
        sale_percent = 10
    elif(price>=100000):
        sale_percent = 5

    return int(price*((100-sale_percent)/100))