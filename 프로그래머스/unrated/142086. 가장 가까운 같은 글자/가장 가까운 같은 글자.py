def solution(s):
    answer = []
    s_idx_dict = {}
    input_num = -1
    for i,c in enumerate(s):
        if c in s_idx_dict:
            input_num = abs(s_idx_dict[c] - i)
        else:
            input_num = -1
        s_idx_dict[c] = i
        answer.append(input_num)
    return answer