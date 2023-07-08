case_cnt = 0
while True:
    case_cnt += 1
    l,p,v = map(int,input().split())
    answer = 0
    if l == 0 and p == 0 and v == 0:
        break
    answer += (v // p) * l
    if v % p > l:
        answer += l
    else:
        answer += v % p
    print(f"Case {case_cnt}: {answer}")