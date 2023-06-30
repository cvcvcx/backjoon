import sys
input = sys.stdin.readline
def isPrime(n):
    if n<2:
        return False
    for num in range(2,int(n**0.5)+1):
        if n % num == 0:
            return False
    return True

max_ = 246912
dict_ = {i:True for i in range(max_+1)}
for key,value in dict_.items():
    dict_[key] = isPrime(key)
while True:
    num = int(input().strip())
    if num == 0:
        exit()
    counter = 0
    for n in range(num+1, 2*num+1):
        if dict_[n]:
            counter += 1
    print(counter)
            