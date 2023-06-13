def solution(id_list, report, k):
    answer = [0]*len(id_list)
    report_id_set_arr = [set() for _ in range(len(id_list))]
    for i in range(len(report)):
        reported_man = report[i].split()[1]
        report_man = report[i].split()[0]
        report_id_set_arr[id_list.index(reported_man)].add(report_man)
    for report_id_set in report_id_set_arr:
        if(len(report_id_set)>=k):
            for report_id in report_id_set:
                answer[id_list.index(report_id)] += 1
    
    return answer