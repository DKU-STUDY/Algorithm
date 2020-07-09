def solution(name_list):

    for i in range (len(name_list)):
        for j in range (i+1, len(name_list)):
            if(name_list[i]==name_list[j]):
                return True
            elif(len(name_list[i])<len(name_list[j])):
                print(name_list[i], name_list[j])
                tmp=list(name_list[j])
                print(tmp)
                for k in tmp:
                    if(k==name_list[i]):
                        return True
    return False


if __name__=="__main__":
    name_list=["가을", "우주", "너굴"]
    name_list1=["봄", "여울", "봄봄"]
    print(solution(name_list1) )
