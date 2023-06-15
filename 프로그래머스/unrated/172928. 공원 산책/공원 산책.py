def make_park_list(park):
    park_list = []
    for item in park:
        park_list.append(list(item))
    return park_list

def find_start(park_list,S):
    for i in range(len(park_list)):
        for j in range(len(park_list[i])):
            if park_list[i][j] == S:
                return [i,j]
def set_dir_num(dir):
    dir_num = 0
    if dir == "N":
        dir_num = 0
    elif dir == "E":
        dir_num = 1
    elif dir == "S":
        dir_num = 2
    elif dir == "W":
        dir_num = 3
    return dir_num

#now에서 route의 명령대로 이동 -> now에 이동한 값 대입
def move(park_list,now,route):
    # N = 0 E = 1 S = 2 W = 3 
    directionY = [-1,0,1,0] 
    directionX = [0,1,0,-1]
    
    dir, dis =  route.split()
    dir_num = set_dir_num(dir)
    start = now
    calculation_end_Y = now[0]+(directionY[dir_num])*int(dis)
    calculation_end_X = now[1]+(directionX[dir_num])*int(dis)
    print("now = ",now)
    print("calculation = ",[calculation_end_Y,calculation_end_X])
    
    if calculation_end_Y > len(park_list)-1 or calculation_end_Y < 0:
        return start
    
    if calculation_end_X > len(park_list[0])-1 or calculation_end_X < 0:
        return start
    
    for i in range(int(dis)):
        calculationY = now[0]+(directionY[dir_num])*i
        calculationX = now[1]+(directionX[dir_num])*i
        
        if park_list[calculationY][calculationX] == "X":
            return start
        
    for _ in range(int(dis)):
        calculationY = now[0]+(directionY[dir_num])
        calculationX = now[1]+(directionX[dir_num])
        if calculationY < len(park_list) and calculationY >-1 :
            if calculationX < len(park_list[calculationY]) and calculationX >-1:
                if park_list[calculationY][calculationX] == "O":
                    now = [calculationY,calculationX]
                elif park_list[calculationY][calculationX] == "S":
                    now = [calculationY,calculationX]
                elif park_list[calculationY][calculationX] == "X":
                    now = start
                
    return now
    
    
def solution(park, routes):
    
    S = "S"
    X = "X"
    
    park_list = make_park_list(park)
    start = find_start(park_list,S)
    now = start
    
    for route in routes:
        now = move(park_list,now,route)
        
    return now

