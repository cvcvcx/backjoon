def solution(babbling):
    answer = 0
    say_list = ["aya","ye","woo","ma"]
    for b in babbling:
        for s in say_list:
            b = b.replace(s,"!",1)
        if b.replace("!","") == "":
            answer += 1
    return answer