n = 10000
answer = set(range(1,n+1))
not_self_num = set()
for num in range(1,n+1):
    s_num = str(num)
    sum_result = num
    for s in s_num:
        sum_result += int(s)
    not_self_num.add(sum_result)
result = answer - not_self_num
result_list = list(result)
result_list.sort()
for r in result_list:
    print(r)