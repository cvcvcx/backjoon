def solution(players, callings):
    player_dic = {player:i for i, player in enumerate(players)}
    
    for call in callings:
        cur_idx = player_dic[call]
        pre_idx = cur_idx-1
        
        player_dic[call] -= 1
        player_dic[players[pre_idx]] += 1
        
        temp = players[pre_idx]
        players[pre_idx] = players[cur_idx]
        players[cur_idx] = temp
        
        
    return players