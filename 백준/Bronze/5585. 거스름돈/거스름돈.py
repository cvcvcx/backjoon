change_list = [500,100,50,10,5,1]
n = int(input())
bill = 1000
change = bill - n
result = 0
for c in change_list:
    result += change // c
    change = change % c
print(result)