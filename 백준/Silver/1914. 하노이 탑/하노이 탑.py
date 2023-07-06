#3개의 원판을 옮긴다.
n = int(input())
def move_tower(from_, to, aux, m):
    if m == 1:
        print(from_,to)
    else:
        #m-1원판을 이동시킨다.
        move_tower(from_, aux, to, m - 1)
        #m - 1의 이동이 전부 끝나고 나서, 제일 큰 원판을 목표지점으로 옮긴다.
        print(from_, to)
        #이제 보조기둥에 있던 m-1크기의 원판들을 to로 옮긴다.
        move_tower(aux, to, from_, m - 1)
print(2**n-1)
if n<=20:
    move_tower(1,3,2,n)