def solution(keymap, targets):
    answer = []
    for t in targets:
        idx_sum =0
        for c in t:
            idx_list = []
            for map_ in keymap:
                if c in map_:
                    idx_list.append(map_.index(c)+1)
            if idx_list:
                idx_sum += min(idx_list)
            else:
                idx_sum = -1
                break
        answer.append(idx_sum)
    return answer