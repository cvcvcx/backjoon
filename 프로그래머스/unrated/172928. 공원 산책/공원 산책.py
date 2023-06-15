def solution(park, routes):
    dy = {"N":-1,"E":0,"S":1,"W":0}
    dx = {"N":0,"E":1,"S":0,"W":-1}
    
    # 맵의 크기를 변수로 만든다.
    N,M = len(park),len(park[0])
    # 시작점을 찾는다
    y,x=0,0
    #이중배열을 순환하면서 S를 찾는다.
    for i in range(N):
        for j in range(M):
            if park[i][j] == "S":
                #찾으면 y,x에 인덱스를 집어넣는다.
                y,x = i,j
    
    #routes를 순환하면서 이동거리와 방향을 가지고 이동시켜본다.
    for route in routes:
        dir_,dist = route.split()
        #이동이 유효한지 판별하는 boolean값
        move_is_false = False
        
        # 1~dist, 그러니까 목적지까지 직선으로 장애물이 있는지 없는지 확인 및 맵을 벗어나는지 확인
        for i in range(1, int(dist)+1):
            ny,nx = y+dy[dir_]*i,x+dx[dir_]*i
            
            #맵 밖으로 나갔는지 확인
            if ny < 0 or nx < 0 or ny > N-1 or nx > M-1:
                move_is_false = True
                break
            #X를 지나가는지 확인
            if park[ny][nx] == "X":
                move_is_false = True
                break
            
        if move_is_false == True:
            continue
        else:
            ny,nx = y+dy[dir_]*int(dist),x+dx[dir_]*int(dist)
            y,x = ny,nx
    
            
    
    
    answer = [y,x]
    return answer