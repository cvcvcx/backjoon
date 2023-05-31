student = []
for i in range(30):
    student.append(i+1)
for _ in range(28):
    input_num = int(input())
    student.remove(input_num)
for item in student:
    print(item)