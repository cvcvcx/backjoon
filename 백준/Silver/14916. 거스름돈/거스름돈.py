'''
1. 아이디어
    while문을 돌면서, 2의 개수를 늘려가면서, 만약 5로 나누어 떨어진다면 바로 프린트
2. 시간복잡도
    O(n)
    for문 한번만 돌면 될듯?
3. 자료구조
'''
n = int(input())

result = -1
two_cnt = 0
while two_cnt * 2 <= n:
    if (n - (two_cnt * 2)) % 5 == 0:
        result = two_cnt + ((n - (two_cnt * 2)) // 5)
        break
    two_cnt += 1
print(result)