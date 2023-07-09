'''
1. 아이디어
    1.레벨의 수 n개 주어짐
    2.아래로 내려갈 수록 어렵고, 점수를 많이 줘야함
    3.하지만 실수로 쉬운 난이도가 더 점수를 많이 주는 경우가 발생
    4.제대로 된 점수 체계로 돌려야함

    맨 아래에 있는 수를 기준으로, 위 숫자들을 감소시켜나가면 됨
    ---
    맨 아래에 있는 수를 기준으로 작으면 그 수를 기준으로 다시 삼고, 아니라면 기준보다 -1 시킨 수만큼answer에 더함
    맨 아래에서 두번째는 max_n -1, max_n - 2 이런식으로 해서, 원래 수와의 차이를 비교하여 answer에 넣음
2. 시간복잡도
    for문 한번이면 될듯 O(n)
3. 자료구조
    레벨 수 n : int
    원래의 점수체계 score_list : int[]
    max_score : int
'''
n = int(input())
score_list = [int(input()) for _ in range(n)]
max_score = score_list[len(score_list)-1]
answer = 0
# 최대치(배열의 끝)는 반복문에서 빠져야지 정확한 수치가 나옴
# 그래서 범위를 2부터 시작하게끔 함 (n이 3인경우, [2]가 최대치가 되므로, [1]의 값부터 비교할 수 있게끔
# 항상 그리디는 범위를 제대로 정하는것이 중요한듯!
for i in range(2,n+1):
    if score_list[n-i] < max_score:
        max_score = score_list[n-i]
    elif score_list[n-i] >= max_score:
        max_score -= 1
        answer += score_list[n-i] - max_score
print(answer)