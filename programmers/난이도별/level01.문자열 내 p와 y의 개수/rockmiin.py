def solution(s):
    cnt_p=0; cnt_y=0
    for i in s:
        if i == 'P' or i=='p':
            cnt_p+=1
        if i == 'Y' or i == 'y':
            cnt_y+=1
    if cnt_p==cnt_y: return True
    return False

solution('pPoooyY')