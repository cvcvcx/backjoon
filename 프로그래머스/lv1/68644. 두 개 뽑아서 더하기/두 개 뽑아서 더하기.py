def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            if i != j :
                print(numbers[i],numbers[j])
                answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    
    return answer