test_count = int(input())
for _ in range(test_count):
    repeat, s = input().split()
    text = ""
    for i in s:
        text += int(repeat) * i
    print(text)