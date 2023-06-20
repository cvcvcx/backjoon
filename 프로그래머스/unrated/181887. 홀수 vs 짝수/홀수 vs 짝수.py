def solution(num_list):
    odd_ = sum(num_list[::2])
    even_ = sum(num_list[1::2])
    return max(odd_,even_)