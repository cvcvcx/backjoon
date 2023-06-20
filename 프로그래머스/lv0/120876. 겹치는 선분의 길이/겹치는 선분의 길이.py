def solution(lines):
    answer = 0
    for idx in range(0,3):
        l1,l2 = lines[idx-1],lines[idx]
        l1s,l1e = l1[0],l1[1]
        l2s,l2e = l2[0],l2[1]
        start_max = max(l1s,l2s)
        end_min = min(l1e,l2e)
        if end_min > start_max:
            answer += end_min - start_max
    l1,l2,l3 = lines[0],lines[1],lines[2]
    
    l1s,l1e = l1[0],l1[1]
    l2s,l2e = l2[0],l2[1]
    l3s,l3e = l3[0],l3[1]
    start_max = max(l1s,l2s,l3s)
    end_min = min(l1e,l2e,l3e)
    if end_min > start_max:
            answer -= (end_min - start_max)*2
    return answer