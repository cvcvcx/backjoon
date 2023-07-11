n = int(input())
s = input()
while "LL" in s:
    s = s.replace("LL","X")
max_v = len(s)+1
if n < max_v:
    print(n)
else:
    print(max_v)