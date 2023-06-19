student = []
for i in range(1,30+1):
    student.append(i)
for _ in range(28):
    x = int(input())
    student.remove(x)
for s in student:
    print(s)