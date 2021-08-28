class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        # 최대값. 실제로는 이보다 작음. 넉넉히 잡음
        arr = [[] for _ in range(len(num1) + len(num2))]

        for i in range(len(num1)):
            for j in range(len(num2)):
                num = int(num1[i]) * int(num2[j])
                arr[i + j + 1].append(num // 10)
                arr[i + j].append(num % 10)

        ans = ""
        # sum을 해결하자.
        carry = 0
        for s in arr:
            num = sum(s) + carry
            carry = num // 10
            ans = str(num % 10) + ans

        pos = 0
        # 마지막 0 제외.  앞에서 부터 0제외
        while pos < len(ans) - 1 and ans[pos] == '0':
            pos += 1

        return ans[pos:]