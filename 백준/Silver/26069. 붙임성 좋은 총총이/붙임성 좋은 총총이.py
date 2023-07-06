n = int(input())
dance_people_set = {"ChongChong"}
for _ in range(n):
    a, b = input().split()
    if a in dance_people_set or b in dance_people_set:
        dance_people_set.add(a)
        dance_people_set.add(b)
print(len(dance_people_set))