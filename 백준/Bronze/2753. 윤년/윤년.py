
year = int(input())
result = 0
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    result = 1
else :
    resut = 0
print(result)