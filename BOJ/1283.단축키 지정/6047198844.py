N = int(input())
options = [input() for _ in range(N)]
shortcuts = set()

for option in options:
    words = option.split()
    # 1. 먼저 하나의 옵션에 대해 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다. 만약 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정한다.
    for idx, word in enumerate(words):
        if word[0].isalpha() and word[0].upper() not in shortcuts:
            shortcuts.add(word[0].upper())
            words[idx] = '[' + words[idx][0] + ']' + words[idx][1:]
            print(' '.join(words))
            break
    # 2. 만약 모든 단어의 첫 글자가 이미 지정이 되어있다면 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정한다.
    else:
        for idx, char in enumerate(option):
            if char.isalpha() and char.upper() not in shortcuts:
                shortcuts.add(char.upper())
                print(option[:idx] + '[' + char + ']' + option[idx + 1:])
                break
        else:
            print(option)
