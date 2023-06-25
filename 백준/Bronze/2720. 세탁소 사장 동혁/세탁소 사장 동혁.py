T = int(input())
changes = [25,10,5,1]
change_list = [[0] * 4 for _ in range(T)]
for i in range(T):
    p = int(input())
    for j in range(len(changes)):
        if changes[j] != 1:
            change_list[i][j] = p // changes[j]
            p = p%changes[j]
        else:
            change_list[i][j] = p
        print(change_list[i][j], end = " ")
    print()
