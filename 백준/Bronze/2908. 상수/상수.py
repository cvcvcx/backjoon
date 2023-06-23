a, b = map(int,input().split())

str_a = (str(a))
str_b = (str(b))

str_a = str_a[::-1]
str_b = str_b[::-1]
if int(str_a) < int(str_b):
    print(str_b)
elif int(str_a) > int(str_b):
    print(str_a)