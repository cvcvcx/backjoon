def solution(numbers, hand):
    answer = ''
    # 1,4,7 일경우 무조건 l_hand가 움직임
    # 3,6,9 일경우 무조건 r_hand가 움직임
    # 2,5,8,0 일경우 l_hand - num r_hand-num을 비교함
    # 같은 거리일경우, 자주쓰는 손가락으로 사용
    
    l_hand = 10
    r_hand = 12
    
    for num in numbers:
        if num in [1,4,7]:
            answer += "L"
            l_hand = num
        elif num in [3,6,9]:
            answer += "R"
            r_hand = num
        else:
            cal_num = num
            if num == 0:
                cal_num = 11
            l_dis = abs(l_hand-cal_num)//3 + abs(l_hand-cal_num)%3
            r_dis = abs(r_hand-cal_num)//3 + abs(r_hand-cal_num)%3
            
            if  l_dis>r_dis:
                answer += "R"
                r_hand = cal_num
            elif l_dis<r_dis:
                answer += "L"
                l_hand = cal_num
            else:
                if hand == "right":
                    answer += "R"
                    r_hand = cal_num
                else:
                    answer += "L"
                    l_hand = cal_num
    return answer