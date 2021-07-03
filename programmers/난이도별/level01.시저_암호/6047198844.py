def solution(s, n):
    answer = ''

    for char in s:
        # 공백이면 안민다.
        if str.islower(char):
            char = chr(ord('a') + (ord(char) - ord('a') + n) % 26)
        elif str.isupper(char):
            char = chr(ord('A') + (ord(char) - ord('A') + n) % 26)
        answer += char

    return answer