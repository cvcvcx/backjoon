'''
1. 아이디어
    1. 로프의 개수
    2. 로프가 견딜 수 있는 중량
    
    경우의 수 3개의 로프가 주어졌을 때, 3 * 최소치가 더 큰 경우
    3개의 로프가 주어졌을 때, 2 * 두번째 수가 더 큰 경우
    while문을 돌면서 최소치 * n, 최소치 + 1 * n-1 하면서 가장 큰 값을 저장함
2. 시간복잡도
    while문으로 k의 개수만큼 계산을 해야하기 때문에 O(k)정도? + 정렬이니까 N log N
3. 자료구조
    배열 또는 리스트로 충분할듯?
'''

n = int(input())
num_list = [int(input()) for _ in range(n)]
num_list.sort()
maxv = 0

for i in range(n):
    #0번째면 총 개수 - 0을 최소치와 곱하는 것이기 때문에 아이디어와 일치한다.
    tmp = num_list[i] * (n-i)
    if tmp > maxv:
        maxv = tmp
        
print(maxv)