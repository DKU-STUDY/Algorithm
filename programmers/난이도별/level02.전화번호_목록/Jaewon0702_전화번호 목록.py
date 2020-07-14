def solution(phone_book):
    phone_book.sort()
    for j,k in enumerate(phone_book):
        for i,v in enumerate(phone_book):
            if j!=i :
                if k in v :
                    return False
                else :
                    return True
                    
                

p=['119','97674223','119']

print(solution(p))

#채점 결과 : 100점

