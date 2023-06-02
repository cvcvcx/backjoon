def solution(money):
    answer = []
    coffee_price = 5500
    coffee_count = money // coffee_price
    coin = money % coffee_price
    answer=[coffee_count,coin]
    return answer