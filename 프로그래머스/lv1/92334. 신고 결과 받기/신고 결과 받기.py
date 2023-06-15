def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported_id_dic = {id:0 for id in id_list}
    
    #신고당한 유저의 dic의 value에 += 1
    for r in set(report):
        reported_id_dic[r.split()[1]] += 1
    #set(report)에 있는 값들을 순회하면서 신고횟수가 k 이상인 값을 찾기
    for r in set(report):
        if reported_id_dic[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer