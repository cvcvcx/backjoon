n = int(input())
num = 1
prev = 0
idx = 0

while True:
    if (n-1) / 6 > prev:
        idx += 1
        prev = idx + prev
    else:
        idx += 1
        break
print(idx)