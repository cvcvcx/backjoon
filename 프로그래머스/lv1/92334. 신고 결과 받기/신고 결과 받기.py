def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported_id_dic = {id:[] for id in id_list}
    
    #신고당한 유저의 dic의 value에 += 1
    for r in set(report):
        report_man = r.split()[0]
        reported_man = r.split()[1]
        reported_id_dic[reported_man].append(report_man)
    #dic.items()에 있는 값들을 순회하면서 신고횟수가 k 이상인 값을 찾기
    for key,value in reported_id_dic.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1
    
    return answer