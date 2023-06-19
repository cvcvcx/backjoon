light,com = map(int,input().split())

light_list = list(map(int,input().split()))

for i in range(com):
    c,x,y = map(int,input().split())
    if c == 1:
        light_list[x-1] = y
    elif c == 2:
        for l in range(x-1,y):
            if light_list[l] == 0:
                light_list[l] = 1
            else:
                light_list[l] = 0
    elif c == 3:
        for l in range(x-1,y):
            light_list[l] = 0
    elif c == 4:
        for l in range(x-1,y):
            light_list[l] = 1
answer = ''
for l in range(len(light_list)):
    answer += str(light_list[l])
    if l < len(light_list)-1:
        answer += " "
        
print(answer)
    
            