def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j and phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                return False
    return True

print(
    solution(['119', '97674223', '1195524421']) == False,
    solution(['123', '456', '789']) == True,
    solution(['12', '123', '1235', '567', '88'])
)