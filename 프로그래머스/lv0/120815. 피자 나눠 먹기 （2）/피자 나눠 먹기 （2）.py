def solution(n):
    piece = 6
    
    return lcm(n,piece)//piece

def gdc(x,y):
    while y>0:
        x,y = y, x%y
    return x

def lcm(x,y):
    return (x*y) / gdc(x,y)