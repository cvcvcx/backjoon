# 자주 나오는 단어일수록 앞에 배치
# 해당 단어의 길이가 길수록 앞에 배치
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
word_dic = {}
for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    else:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
set_word_list = sorted(word_dic.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
for s in set_word_list:
    print(s[0])
