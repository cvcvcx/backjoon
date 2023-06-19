import sys
board = {}
check = [[0] * 5 for _ in range(5)]
for i in range(5):
    b_num_list = list(map(int, input().split()))
    for j in range(len(b_num_list)):
        board[b_num_list[j]] = (i, j)
count = 0

for _ in range(5):
    m_num_list = list(map(int, input().split()))
    for i in range(len(m_num_list)):
        count += 1

        if m_num_list[i] in board:
            check[board[m_num_list[i]][0]][board[m_num_list[i]][1]] = 1
            bingo_count = 0

            for j in range(5):
                if sum(check[j]) == 5:
                    bingo_count += 1
                if sum([k[j] for k in check]) == 5:
                    bingo_count += 1
            if check[0][4] + check[1][3] + check[2][2] + check[3][1] + check[4][0] == 5:
                bingo_count += 1
            if check[0][0] + check[1][1] + check[2][2] + check[3][3] + check[4][4] == 5:
                bingo_count += 1
            if bingo_count >= 3:
                print(count)
                sys.exit()



