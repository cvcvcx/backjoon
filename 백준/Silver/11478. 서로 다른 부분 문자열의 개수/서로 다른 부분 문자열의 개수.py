s = input()
_set = set()

for i in range(len(s)):
    for j in range(i,len(s)):
        _set.add(s[i:j+1])
print(len(_set))