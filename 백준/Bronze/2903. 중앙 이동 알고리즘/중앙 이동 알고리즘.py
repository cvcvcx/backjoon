n = int(input())
width_list = [2]
dot_list = [4]

for i in range(1,n+1):
    w = width_list[i-1] + width_list[i-1] - 1
    width_list.append(w)
    dot = w ** 2
    dot_list.append(dot)
    
print(dot_list[n])
    