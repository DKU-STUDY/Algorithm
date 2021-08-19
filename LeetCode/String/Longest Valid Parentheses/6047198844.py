class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        if N <= 1:
            return 0

        longest = [0] * N

        # dp 사용
        # longest[idx]에는 s[idx]로 끝나는 Longest Valid Parentheses중 가장 긴 길이가 저장된다.
        for idx in range(1, N):
            # '('로 끝나는 Valid Parentheses는 없다.
            if s[idx] == '(':
                longest[idx] = 0
            else:  # ')'로 끝나는 Valid Parentheses가 되려면. 직전 Longest Valid Parentheses의 앞 괄호가 '('이여야한다.
                if idx - 1 - longest[idx - 1] >= 0 and s[idx - 1 - longest[idx - 1]] == '(':
                    # '(' + Longest Valid Parentheses길이 + ')'
                    longest[idx] = 1 + longest[idx - 1] + 1
                    # 범위가 된다면, 바로 직전의 Longest Valid Parentheses도 더해준다.
                    if idx - 1 - longest[idx - 1] - 1 >= 0:
                        longest[idx] += longest[idx - 1 - longest[idx - 1] - 1]

        return max(longest)