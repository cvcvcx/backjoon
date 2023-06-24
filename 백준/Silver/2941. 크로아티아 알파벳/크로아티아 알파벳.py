croa = ["c=","c-","dz=","d-","lj","nj","s=","z="]

s = input()
for c in croa:
    if c in s:
        s = s.replace(c,"a")
print(len(s))
    