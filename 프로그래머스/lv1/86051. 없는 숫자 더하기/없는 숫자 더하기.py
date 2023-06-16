def solution(numbers):
    num_set = {i for i in range(10)}
    numbers_set = set(numbers)
    num_set -= numbers_set
    return sum(num_set)