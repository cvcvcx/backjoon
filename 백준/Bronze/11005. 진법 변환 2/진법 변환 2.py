N, B = map(int,input().split())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_num_dict = {10+i:al for i,al in enumerate(alpha)}

reverse_result = ""
while N>0:
    if N % B >9:
        reverse_result += alpha_num_dict[N%B]
    else:
        reverse_result += str(N%B)
    N = N // B
print(reverse_result[::-1])