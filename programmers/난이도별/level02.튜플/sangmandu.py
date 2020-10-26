def solution(s):
    s = s[1:-1]
    lst = []
    while True:
        a = s.find('},')
        if a != -1:
            lst.append(s[1:a])
            s = s[a+2:]
            continue
        break
    lst.append(s[1:-1])    
    
    for i in range(len(lst)):
        lst[i] = lst[i].split(',')
    
    lst2 = sum(lst, [])
    for i in range(len(lst2)):
        lst2[i] = int(lst2[i])
    
    answer = [0 for i in range(len(set(lst2)))]
    for i in set(lst2):
         answer[lst2.count(i)-1] += i   
    answer.reverse()
    
    return answer
