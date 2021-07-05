col = [True] * 50
row = [True] * 50
left_diag = [True] * 50
right_diag = [True] * 50

def dfs(r, n):
    if r == n:
        return 1
    ans = 0
    for c in range(n):
        if col[c] and row[r] and left_diag[c+r] and right_diag[n-1+r-c]:
            col[c] = False
            row[r] = False
            left_diag[c+r] = False
            right_diag[n-1+r-c] = False
            ans += dfs(r+1, n)
            right_diag[n-1+r-c] = True
            left_diag[c+r] = True
            row[r] = True
            col[c] = True
    return ans
            
    
def solution(n):
    return dfs(0, n)