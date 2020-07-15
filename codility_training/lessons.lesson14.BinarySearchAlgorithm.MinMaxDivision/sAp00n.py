def solutnion(K, M, A):
    lenA = len(A)
    low, high = M, sum(A)
    middle = int((low + high) / 2)
    curser = -1
    while True:
        print(f'low: {low}    middle: {middle}     high: {high}')
        curser += 1
        for subunit_num in range(0, K):
            print(f'subunit_Num : {subunit_num}')
            subunit_sum = 0
            search_condition = True
            over_condition = True
            while search_condition:
                # 커서는 list의 끝까지 도착했지만, subunit은 다 만들어지지 않은 경우 => middle 이 최적해보다 크다.
                print(f'    curser : {curser}')
                if curser == lenA - 1 and subunit_num < K-1:
                    search_condition = False
                    over_condition = False  # 이중 loop 탈출 조건 설정
                    temp = middle
                    middle = int((low + middle) / 2)
                    high = temp
                    curser = -1
                    print(f'condition 01 in')

                elif subunit_sum + A[curser] > middle:
                    search_condition = False
                    #curser -= 1
                else:
                    subunit_sum += A[curser]
                    print(f'    subunit_sum : {subunit_sum}     added : {A[curser]}')
                    curser += 1

            if not over_condition:
                break
        if curser == lenA-1 and subunit_num == K - 1:
            return middle
        # for loop 를 탈출해 모든 subunit이 만들어졌지만, curser는 리스트의 끝에 가지 못한경우 => middle이 최적해보다 작다.
        if curser != lenA - 1:
            print(f'condition 02 in')
            temp = middle
            middle = int((high + middle) / 2)
            low = temp



A = [2, 1, 5, 1, 2, 2, 2]
print(solutnion(3, 5, A))
