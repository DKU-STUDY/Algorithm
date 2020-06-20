def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        
        array = ""
        binary1 = bin(arr1[i])[2:]
        binary2 = bin(arr2[i])[2:]
        if len(binary1) < n:
            binary1 = "0" * (n-len(binary1)) + binary1
        if len(binary2) < n:
            binary2 = "0" * (n-len(binary2)) + binary2
        for j in range(n):
            if binary1[j] == '1' or binary2[j] == '1':
                array += "#"
            else:
                array += " "
        answer.append(array)
    return answer
    
print(solution( 5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]) == \
    ["#####", "# # #", "### #", "#  ##", "#####"])
print(solution(	6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]) == \
    ["######", "###  #", "##  ##", " #### ", " #####", "### # "])
