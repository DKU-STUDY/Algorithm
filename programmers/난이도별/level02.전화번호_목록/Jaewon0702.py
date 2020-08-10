def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)) :
        for v in phone_book[i:] :
            if phone_book[i]!=v :
                return not phone_book[i] in v
    return True
                    
p=['119','97674223','119']

print(solution(p))

#채점 결과 : 100점

