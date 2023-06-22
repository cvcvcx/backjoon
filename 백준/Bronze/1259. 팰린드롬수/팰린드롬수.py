import sys
input = sys.stdin.readline
while True:
    n = str(int(input().strip()))
    if n=="0":
        break
        
    count_ = 0
    for i in range(len(n)//2):
        if n[i] == n[-(i+1)]:
            continue
        else:
            count_ += 1
    if count_ == 0:
        print("yes")
    else:
        print("no")
    