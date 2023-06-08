line_number = int(input())
for i in range(line_number):
    for j in range(line_number-i-1):
        print(" ", end = "")
    for k in range(2*i+1):
        print("*", end = "")
    print()    
    