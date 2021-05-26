N = int(input())
marbles = list(map(int, input().split()))


def dfs(marbels:list, acc:int):
    if len(marbles) == 2:
        return acc

    res = 0
    for idx in range(1,len(marbles)-1):
        tmp = marbels.pop(idx)
        res = max(res,dfs(marbels, acc + marbels[idx-1] * marbels[idx]))
        marbels.insert(idx,tmp)
    return res

print(dfs(marbles,0))