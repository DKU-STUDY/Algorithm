import itertools
from collections import defaultdict


def solution(orders, course):
    ans= []
    # dict 안에 없는 key값이더라도 자동으로 추가해주려고 defaultdict를 사용
    menu_dict= [defaultdict(lambda :0) for _ in range(len(course))]

    for idx in range(len(course)):
        for menu in orders:
            # sorted를 안해주게 되면 WX와 XW를 다른 메뉴로 구분하게 됨
            menu_list= sorted(list(menu))

            if len(menu_list) < idx:
                continue
            # "".join을 사용하면 리스트를 문자열로 쉽게 변환할 수 있다
            for k in list(itertools.combinations(menu_list, course[idx])):
                menu_dict[idx]["".join(k)]+=1

    for idx in range(len(course)):
        #  menu_dict에서 최대값과 같은 모든 key 값을 ans에 append
        for k, v in menu_dict[idx].items():
            if v== max(menu_dict[idx].values()) and v>1:
                ans.append(k)

    return sorted(ans)



solution(["XYZ", "XWY", "WXA"], [2,3,4])