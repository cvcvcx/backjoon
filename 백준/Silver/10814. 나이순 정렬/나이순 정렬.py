n = int(input())
user_list = []

for _ in range(n):
    year, name = input().split()
    year = int(year)
    user_list.append((year,name))

user_list.sort(key = lambda x : x[0])
for user in user_list:
    print(user[0],user[1])