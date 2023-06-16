def solution(players, callings):
    p_rank_dict = {player: i for i,player in enumerate(players)}
    rank_p_dict = {i: player for i,player in enumerate(players)}
    
    for call in callings:
        cur_idx = p_rank_dict[call]
        pre_idx = cur_idx - 1
        
        cur_player = call
        pre_player = rank_p_dict[pre_idx]
        
        rank_p_dict[pre_idx],rank_p_dict[cur_idx] = rank_p_dict[cur_idx],rank_p_dict[pre_idx]
        p_rank_dict[cur_player],p_rank_dict[pre_player] = p_rank_dict[pre_player], p_rank_dict[cur_player]
    
    answer = list(rank_p_dict.values())
    return answer