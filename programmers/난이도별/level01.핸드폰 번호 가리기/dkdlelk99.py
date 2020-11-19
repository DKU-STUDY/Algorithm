def solution(phone_number):
    answer = phone_number.replace(phone_number[0:-4],'*'*len(phone_number[0:-4]))
    return answer
   
print(solution('0222925077') == '******5077')
print(solution('01092295169') == '*******5169')
