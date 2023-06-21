def solution(id_pw, db):
    answer = ''
    id_pw_dict = {id_:pw_ for id_,pw_ in db}
    
    id_,pw_ = id_pw
    
    if id_ in list(id_pw_dict.keys()):
        if id_pw_dict[id_] == pw_:
            answer = "login"
        else:
            answer = "wrong pw"
    else:
        answer = "fail"
    
    return answer