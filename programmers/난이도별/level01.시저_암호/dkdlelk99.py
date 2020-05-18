def solution(s, n):
    small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z']
    big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
            'S','T','U','V','W','X','Y','Z']
    answer = []
    for i in s:
        if i.islower():
            a = small.index(i)
            answer.append(small[(a+n)%26])
        elif i.isupper():
            b = big.index(i)
            answer.append(big[(b+n)%26])
        else:
            answer.append(' ')
    return ''.join(answer)

print(solution('sdf Z',1) == 'teg A')
print(solution('a B z',4) == 'e F d')
