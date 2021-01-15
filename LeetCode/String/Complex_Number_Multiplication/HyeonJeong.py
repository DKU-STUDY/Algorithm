class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        cnt = a.find('+')
        x = [int(a[0:cnt]), int(a[cnt+1:-1])]
        cnt = b.find('+')
        y = [int(b[0:cnt]), int(b[cnt+1:-1])]

        n1 = x[0]*y[0] - x[1]*y[1]
        n2 = x[0]*y[1] + x[1]*y[0]
        answer = str(n1) + "+" + str(n2) + "i"
        return answer