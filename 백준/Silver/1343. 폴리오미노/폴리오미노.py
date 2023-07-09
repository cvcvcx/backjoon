'''
1. 아이디어
 주어진 문자열 리스트로 만들기
 - 일단 .을 기준으로 문자열을 나눠야한다.
 - split으로 나누고싶지만, 그냥은 안됨
 - replace를 통해 .. 을 .으로 바꾸고 리스트를 생성하자

 4와 2로 나눈 몫을 통해 새로운 문자열 리스트 만들기
 - X_list를 구했다. 이 리스트중, len%2가 0이아닌게 하나라도 있다면, -1을 출력하고 반복문을 종료한다.
 - 만약 아니라면, X를 4로 나눈 몫과 나머지를 2로 나눈 몫을 구해야한다. 그래서 새로운 문자열을 만들어서 배열에 저장

 .이 앞에있는지, 아닌지 여부를 통해 .이 들어갈 배열을 구해야한다.
 - 원래 문자열을 따로 저장해서, .의 배열을 따로 구해놓는다.
 - 그리고 dot_first 변수를 통해, 점이 먼전지 아닌지 구한다.

2. 변수
 - 원래 문자열 ori_s
 - ..을 모두 .으로 바꾼 문자열 s
 - ori_s 에서 XX를 X 로 바꾼 문자열 s_x
 - s를 .을 기준으로 나눈 리스트 s_list
 - s_x를 X를 기준으로 나눈 리스트 s_x_list
 - 그리고 ori_s의 맨 첫번째가 "." 이라면 dot_first는 True 아니라면 False

 - 새로운 문자열 리스트 new_s_list
'''

ori_s = input()
s = ori_s
s_x = ori_s
dot_first = False
is_divide = True
if ori_s[0] == ".":
    dot_first = True

while ".." in s:
    s = s.replace("..", ".")
while "XX" in s_x:
    s_x = s_x.replace("XX", "X")

s_list = [c for c in s.split(".") if c]
s_x_list = [x for x in s_x.split("X") if x]
new_list = []

for x in s_list:
    tmp_string = ""
    if len(x) % 2 == 1:
        print(-1)
        is_divide = False
        break
    else:
        tmp_string += "AAAA" * (len(x) // 4)
        tmp_string += "BB" * ((len(x) % 4) // 2)
        new_list.append(tmp_string)

if is_divide:
    if dot_first:
        for i in range(len(s_x_list)):
            print(s_x_list[i], end="")
            if i < len(new_list):
                print(new_list[i], end="")
    else:
        for i in range(len(new_list)):
            print(new_list[i], end="")
            if i < len(s_x_list):
                print(s_x_list[i], end="")
