unique_set = set()
for _ in range(10):
    s = int(input())
    unique_set.add(s%42)
print(len(unique_set))