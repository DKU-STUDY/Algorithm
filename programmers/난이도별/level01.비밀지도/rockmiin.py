
def solution(n, arr1, arr2):
    def combine(arr1, arr2):
        com=['' for _ in range(len(arr1))]
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if(arr1[i][j]==1 or arr2[i][j]==1):
                    com[i]+='#'
                else: com[i]+= ' '
        return com

    def binary(array):
        res=[[0 for _ in range(n)]for _ in range(n)]
        for i in range(len(array)):
            for j in range(n):
                if (array[i] >= pow(2, n - j - 1)):
                    res[i][j] = 1
                    array[i] -= pow(2, n - j - 1)
        return res

    res1= binary(arr1)
    res2= binary(arr2)
    # print(res1)
    # print(res2)
    return combine(res1, res2)



if __name__=="__main__":
    n=5
    arr1=[9, 20, 28, 18, 11]
    arr2=[30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))