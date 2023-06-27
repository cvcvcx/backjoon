n = int(input())

for _ in range(n):
    test_vps = input()
    stack = []
    for s in test_vps:
        if s == "(":
            stack.append(")")
        elif stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(-1)
    if stack:
        print("NO")
    else:
        print("YES")