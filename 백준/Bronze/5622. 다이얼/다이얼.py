alpha = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
word = input()
s = len(word) * 2

for w in word:
    for i in range(len(alpha)):
        if w in alpha[i]:
            s += i+1
print(s)

