def solution(phone_book):
    length = len(phone_book)
    phone_book.sort()
    for i in range(length):
        for j in range(i+1, length):
            if phone_book[j].find(phone_book[i]) >= 0:
                return False
    return True

print(solution(	["119", "97674223", "1195524421"]) == False)
print(solution(['123','456','789']) == True)
print(solution(	["12", "123", "1235", "567", "88"]) == False)
