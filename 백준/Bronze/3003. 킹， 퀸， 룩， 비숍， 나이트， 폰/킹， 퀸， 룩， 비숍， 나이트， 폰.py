piece_list = [1,1,2,2,2,8]
my_piece_list = list(map(int,input().split()))

answer = []

for i in range(len(piece_list)):
    answer.append(piece_list[i]-my_piece_list[i])

for a in answer:
    print(a,end=" ")
    