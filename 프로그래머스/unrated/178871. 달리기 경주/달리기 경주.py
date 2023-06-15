def solution(players, callings):
    player_dic = {player:i for i, player in enumerate(players)}
    rank_dic = {i:player for i,player in enumerate(players)}
    
    for call in callings:
        cur_idx = player_dic[call]
        pre_idx = cur_idx-1
#         pre_idx = cur_idx-1
        
        cur_player = call
        pre_player = rank_dic[pre_idx]
        
        rank_dic[pre_idx] = cur_player
        rank_dic[cur_idx] = pre_player
        
        player_dic[pre_player] = cur_idx
        player_dic[cur_player] = pre_idx
        
        
    return list(rank_dic.values())