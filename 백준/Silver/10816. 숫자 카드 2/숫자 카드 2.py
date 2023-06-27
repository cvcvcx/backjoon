n = int(input())
my_card_list = list(map(int,input().split()))
my_card_count_dict = {}
for card in my_card_list:
    if card in my_card_count_dict:
        my_card_count_dict[card] += 1
    else:
        my_card_count_dict[card] = 1
m = int(input())
q_card_list = list(map(int,input().split()))
answer_list = []
for q in q_card_list:
    if q in my_card_count_dict:
        answer_list.append(my_card_count_dict[q])
    else:
        answer_list.append(0)
print(*answer_list)