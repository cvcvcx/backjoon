def solution(numbers):
    numbers_dict = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
    for n in list(numbers_dict.keys()):
        numbers = numbers.replace(n,str(numbers_dict[n]))
    return int(numbers)