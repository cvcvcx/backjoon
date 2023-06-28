n = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
answer = 0
word = input()
for i,w in enumerate(word):
    answer += 31**i*(alpha.index(w)+1)
print(answer%1234567891)
    