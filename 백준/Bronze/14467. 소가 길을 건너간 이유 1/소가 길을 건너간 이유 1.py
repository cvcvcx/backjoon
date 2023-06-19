count = 0
n = int(input())
cow_dict = {}
for _ in range(n):
    cow, state = map(int,input().split())
    if cow not in cow_dict:
        cow_dict[cow] = state
    else:
        if cow_dict[cow] != state:
            count += 1
            cow_dict[cow] = state
print(count)