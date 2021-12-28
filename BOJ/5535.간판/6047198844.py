# 문제
# 편의점에는 이전 주인이 버리고 간 오래된 간판이 N개 있다. 상근이는 오래된 간판에서 일부 문자를 지워 새로운 간판을 만들려고 한다.
# - 남은 문자열이 편의점 이름이어야 하고, 남은 문자가 모두 일정한 간격으로 떨어져 있어야 한다.
# - 간판을 자르거나 붙일수는 없다.
# - 하나의 오래된 간판에서 만들 수 있는 방법이 여러 개인 경우에도 만들 수 있는 간판은 하나이다.
#
# 입력
# 첫째 줄에 오래된 간판의 수 N이 주어진다. (1 ≤ N ≤ 100) 둘째 줄에는 상근이가 새로 연 편의점의 이름이 주어진다.
# 이름은 알파벳 소문자로만 이루어져 있고, 길이는 3자 이상, 25자 이하이다. 다음 N개 줄에는 이전 주인이 버리고 간 간판에 쓰여 있는 문자가 주어진다. 이 간판에 쓰여 있는 문자는 알파벳 소문자이고, 길이는 1자 이상 100자 이하이다.
#
# 출력
# 첫째 줄에 상근이가 만들 수 있는 간판의 수를 출력한다.
import sys

# 입력
N = int(sys.stdin.readline())
new_signboard = sys.stdin.readline().rstrip()
old_signboards = [sys.stdin.readline().rstrip() for _ in range(N)]

res = 0


def is_possible_to_make(new_signboard, old_signboard):
    for start_idx in range(len(old_signboard)):
        for d in range(1, len(old_signboard)):
            # 끝항이 범위를 넘어서는가?
            end_idx = start_idx + d * (len(new_signboard) - 1)
            board = ""
            if len(old_signboard) <= end_idx:
                break
            for idx in range(start_idx, end_idx + 1, d):
                board += old_signboard[idx]

            if board == new_signboard:
                return True
    return False


for old_signboard in old_signboards:
    # 초항 + d * (n-1)
    res += int(is_possible_to_make(new_signboard, old_signboard))

print(res)
