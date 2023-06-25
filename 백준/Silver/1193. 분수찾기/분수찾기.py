n = int(input())

end = 0
line = 0

x,y = 0, 0

while end<n:
    line += 1
    end += line
    
idx = end - n


if line % 2 != 0:
    x = idx + 1
    y = line - idx
else:
    x = line - idx
    y = idx + 1
    
print(f"{x}/{y}")
            