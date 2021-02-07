import re
from itertools import permutations
def solution(expression):
    ans= 0
    # 정규 표현식으로 num과 op를 나눠줌
    num= re.findall('\d+', expression)
    op= re.findall('[-*+]', expression)
    # order list는 어차피 6개니까 내가 리스트로 줘도 된다 그러면 연산 시간 내려감
    order_list= list(permutations(set(op), len(set(op))))

    # print(num)
    # print(op)
    # print(order_list)

    for order in order_list:
        tmp_num= num[:]
        tmp_op= op[:]
        # print(order)
        for o in order:
            i= 0
            while(i<len(tmp_op)):
                if tmp_op[i]== o:
                    a= tmp_num[i]
                    b= tmp_num.pop(i+1) #없애줘야 len이 줄어 연산 가능
                    # print(str(a)+str(o)+str(b))
                    tmp_num[i]= eval(str(a)+str(o)+str(b))
                    tmp_op.pop(i)
                    i-=1
                    # print(num, op)
                    # print(tmp_num, tmp_op)
                i+=1
        if abs(tmp_num[0])> ans:
            ans= abs(tmp_num[0])
    return ans

print(solution("100-200*300-500+20"))