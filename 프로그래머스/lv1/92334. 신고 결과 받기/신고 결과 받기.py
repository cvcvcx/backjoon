def solution(id_list, report, k):
    answer = [0]*len(id_list)
    
    reported_man_set_arr = [set() for _ in range(len(id_list))]
    
    for r in report:
        report_man = r.split()[0]
        reported_man = r.split()[1]    
        reported_man_set = reported_man_set_arr[id_list.index(reported_man)]
        reported_man_set.add(report_man)
        
    for report_man_set in reported_man_set_arr:
        if len(report_man_set) >= k:
            for man in report_man_set:
                answer[id_list.index(man)] += 1
                
    return answer