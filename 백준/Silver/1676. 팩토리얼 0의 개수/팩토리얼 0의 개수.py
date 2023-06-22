n = int(input())

mul_number = 1
for c in range(1,n+1):
    mul_number = mul_number * c
str_number = str(mul_number)
cnt = 0
reversed_str_number_list = list(reversed(str_number))
for i in range(len(reversed_str_number_list)):
    if reversed_str_number_list[i] == "0":
        cnt += 1
    if reversed_str_number_list[i] != "0":
        break
print(cnt)