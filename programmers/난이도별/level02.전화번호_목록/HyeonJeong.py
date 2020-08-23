def solution(phone_book):
    phone_book.sort(key = len)
    for i, n in enumerate(phone_book):
        for j in range(i + 1, len(phone_book)):
            if n == phone_book[j][0:len(phone_book[i])]:
                return False
    return True

print(
    solution(['119', '97674223', '1195524421']) == False,
    solution(['123', '456', '789']) == True,
    solution(['12', '123', '1235', '567', '88'])
)
