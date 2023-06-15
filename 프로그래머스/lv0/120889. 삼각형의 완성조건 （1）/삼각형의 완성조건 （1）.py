def solution(sides):
    answer = 0
    max_side = max(sides)
    sides.remove(max_side)
    if max_side < sides[0]+sides[1]:
        return 1
    else:
        return 2    