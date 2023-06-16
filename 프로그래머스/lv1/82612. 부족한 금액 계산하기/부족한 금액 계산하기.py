def solution(price, money, count):
    answer = 0
    total_price = 0
    for i in range(1,count+1):
        total_price += i*price
    if money<total_price:
        answer = total_price - money
    else:
        answer = 0
    return answer