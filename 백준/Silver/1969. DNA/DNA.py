'''
1. 아이디어
 자리수마다 가장 많은 문자열을 뽑아 저장한다.
 문자열 리스트를 돌면서, 일치하는 문자의 수가 가장 많은 문자열을 고른다.
 가장 많이 일치하는 문자열이 정답이 되고, 그때, 일치하지 않는 문자의 수가 Hamming Distance가 된다.
2. 자료구조
 A T G C 자리마다 가장 많은 문자를 세서, 새로운 문자열을 만들어야함
 이중배열
'''

n, m = map(int, input().split())

arr = []

# 문자열을 list형식으로 담아준다
for i in range(n):
    arr.append(list(map(str, input())))

cnt, hap = 0, 0
result = ''
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        if arr[j][i] == 'T':
            t += 1
        elif arr[j][i] == 'A':
            a += 1
        elif arr[j][i] == 'G':
            g += 1
        elif arr[j][i] == 'C':
            c += 1
    if max(a,c,g,t) == a:
        result += 'A'
        hap += c + g +t
    elif max(a,c,g,t) == c:
        result += 'C'
        hap += a + g +t
    elif max(a,c,g,t) == g:
        result += 'G'
        hap += a + c +t
    elif max(a,c,g,t) == t:
        result += 'T'
        hap += c + g + a
    
print(result)
print(hap)