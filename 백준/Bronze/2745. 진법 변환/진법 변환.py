alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_n_dict = {al:10+i for i,al in enumerate(alpha)}

N, B = input().split()
B = int(B)
result = 0
for i in range(len(N)):
    if N[i] in alpha:
        result += alpha_n_dict[N[i]] * B**(len(N)-i-1)
    else:
        result += int(N[i]) * B**(len(N)-i-1)
print(result)
