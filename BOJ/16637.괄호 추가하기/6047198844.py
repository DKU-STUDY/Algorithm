import math
import sys


def cal(operand1, operator, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    return operand1 * operand2


def func(idx, s):
    global res
    if idx > N - 1:
        res = max(s, res)
        return

    operator = '+' if idx == 0 else exp[idx - 1]
    if idx != N - 1:
        brace = cal(int(exp[idx]), exp[idx + 1], int(exp[idx + 2]))
        func(idx + 4, cal(s, operator, brace))
    func(idx + 2, cal(s, operator, int(exp[idx])))


N = int(sys.stdin.readline())
exp = list(sys.stdin.readline().rstrip())
res = -math.inf
func(0, 0)
print(res)
