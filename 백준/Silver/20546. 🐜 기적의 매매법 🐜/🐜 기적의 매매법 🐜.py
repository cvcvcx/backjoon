money = int(input())
j_money = money
s_money = money

stock_price = list(map(int,input().split()))

def cal_j_stock(j_money,stock_price):
    j_stock = 0
    for price in stock_price:
        if j_money >= price:
            j_stock += j_money // price
            j_money = j_money % price
    return j_stock * stock_price[len(stock_price)-1]+j_money

def cal_s_stock(s_money,stock_price):
    s_stock = 0
    up_count = 0
    down_count = 0

    for i in range(1,len(stock_price)):
        if stock_price[i-1]<stock_price[i]:
            down_count = 0
            up_count += 1
        elif stock_price[i-1]>stock_price[i]:
            up_count = 0
            down_count += 1
        else:
            up_count = 0
            down_count = 0
        if up_count == 3 and s_stock>0:
            s_money += s_stock*stock_price[i]
            up_count = 0
        if down_count == 3 and s_money >=stock_price[i]:
            s_stock += s_money//stock_price[i]
            s_money = s_money%stock_price[i]
    return s_stock * stock_price[len(stock_price)-1] + s_money

j_last_money = cal_j_stock(j_money,stock_price)
s_last_money = cal_s_stock(s_money,stock_price)

if j_last_money > s_last_money :
    print("BNP")
elif j_last_money < s_last_money:
    print("TIMING")
else:
    print("SAMESAME")