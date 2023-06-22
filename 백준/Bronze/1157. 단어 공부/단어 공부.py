word = input()
word = word.upper()
unique_word = list(set(word))
word_count = []
for w in unique_word:
    word_count.append(word.count(w))
if word_count.count(max(word_count))>1:
    print("?")
else:
    print(unique_word[word_count.index(max(word_count))])