from sys import stdin

N = int(stdin.readline())

cards = list(map(int, stdin.readline().split()))

M = int(stdin.readline())

call_list = list(map(int, stdin.readline().split()))

card_dict = {}

for card in cards:
    card_dict[card] = card_dict.get(card, 0) + 1

return_str = ''
for call in call_list:
    if call not in card_dict:
        return_str += ' 0'
    else:
        return_str += (' '+str(card_dict[call]))

return_str = return_str.strip()
print(return_str)
