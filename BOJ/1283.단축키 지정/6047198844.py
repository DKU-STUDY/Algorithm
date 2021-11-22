N = int(input())
options = [input() for _ in range(N)]
shortcuts = set()

for idx, option in enumerate(options):
    # 1. 먼저 하나의 옵션에 대해 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다. 만약 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정한다.
    for word in option.split():
        if word[0] not in shortcuts:
            shortcuts.add(word[0].upper())
            shortcuts.add(word[0].lower())
            options[idx] = options[idx].replace(word[0], '[' + word[0] + ']', 1)
            break
    # 2. 만약 모든 단어의 첫 글자가 이미 지정이 되어있다면 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정한다.
    else:
        for char in option:
            if char.isalpha() and char not in shortcuts:
                shortcuts.add(char.upper())
                shortcuts.add(char.lower())
                options[idx] = options[idx].replace(char, '[' + char + ']', 1)
                break

for option in options:
    print(option)
