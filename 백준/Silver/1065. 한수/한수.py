n = int(input())

if n < 100:
    result = n
elif n >= 100 and n < 1000:
    result = 99
    for num in range(100,n+1):
        str_num = str(num)
        numbers = list(map(int, list(str_num)))
        if numbers[2]-numbers[1] == numbers[1]-numbers[0]:
            result += 1
elif n == 1000:
    result = 144
print(result)