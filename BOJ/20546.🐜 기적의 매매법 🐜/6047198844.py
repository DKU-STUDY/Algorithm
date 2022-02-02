# 문제
#
# 2099년이 되어도 주식을 팔지 않을 것이다.
# 준현이는 주식을 살 수 있다면 무조건 최대한 많이 산다.
# 준현이는 욕심쟁이이기 때문에, 주식을 살 수 있다면 가능한 만큼 즉시 매수한다. 다음은 준현이가 현금 100원으로 A기업의 주식을 사는 경우이다.
#
#  	1일	2일	3일	4일	5일	6일	7일
# 현금	100	20	20	6	0	0	0
# 주가	40	33	7	2	1	12	50
# 매수 가능 주식 수	2	0	2	3	0	0	0
# 매수여부	O	X	O	O	X	X	X
# 남은 현금	20	20	6	0	0	0	0
# 보유 주식 수	2	2	4	7	7	7	7
# "주식은 타이밍이지!"
#
# 모니터 8개에서 뿜어져 나오는 화려한 주식 차트가 성민이를 감싼다.
# 성민이는 주식이 타이밍 싸움이라 생각한다. 전형적인 단기 투자자로 생각하면 오산이다.
# 이른바 33 매매법으로, 그 방법은 다음의 세 가지 룰로 이루어져있다.
#
# 모든 거래는 전량 매수와 전량 매도로 이루어진다. 현재 가지고 있는 현금이 100원이고 주가가 11원이라면 99원어치의 주식을 매수하는 것이다. 단, 현금이 100원 있고 주가가 101원이라면 주식을 살 수 없다. 성민이는 빚을 내서 주식을 하지는 않는다.
# 3일 연속 가격이 전일 대비 상승하는 주식은 다음날 무조건 가격이 하락한다고 가정한다. 따라서 현재 소유한 주식의 가격이 3일째 상승한다면, 전량 매도한다. 전일과 오늘의 주가가 동일하다면 가격이 상승한 것이 아니다.
# 3일 연속 가격이 전일 대비 하락하는 주식은 다음날 무조건 가격이 상승한다고 가정한다. 따라서 이러한 경향이 나타나면 즉시 주식을 전량 매수한다. 전일과 오늘의 주가가 동일하다면 가격이 하락한 것이 아니다.
# 준현이와 성민이는 각자의 매매법 중 어떤 방법이 더 수익률이 높은지 겨뤄보기로 했다.
# 오로지 MachineDuck이라는 기업의 주식만 거래가 가능하며, 내기 기간은 2021년 1월 1일부터 2021년 1월 14일까지이다. 준현이와 성민이에게 주어진 현금은 동일하다. 세기의 대결이기 때문에 이 기간에는 매일 주식 거래가 가능하다. 2021년 1월 14일에 더 많은 자산을 보유한 사람이 승리한다. 1월 14일의 자산은 (현금 + 1월 14일의 주가 × 주식 수)로 계산한다.
#
# 우리는 2021년 1월 1일부터 2021년 1월 14일까지의 주식 가격을 미리 알고 있다. 준현이와 성민이 중 누가 더 높은 수익률을 낼지 맞혀보자!
#
# 입력
# 첫 번째 줄에 준현이와 성민이에게 주어진 현금이 주어진다.
#
# 두 번째 줄에 2021년 1월 1일부터 2021년 1월 14일까지의 MachineDuck 주가가 공백을 두고 차례대로 주어진다. 모든 입력은 1000 이하의 양의 정수이다.
#
# 출력
# 1월 14일 기준 준현이의 자산이 더 크다면 "BNP"를, 성민이의 자산이 더 크다면 "TIMING"을 출력한다.
#
# 둘의 자산이 같다면 "SAMESAME"을 출력한다. 모든 결과 따옴표를 제외하고 출력한다.

jun_money = sung_money = int(input())
jun_stock = sung_stock = 0
MachineDucks = list(map(int, input().split()))

# 준현이
for MachineDuck in MachineDucks:
    quantity = jun_money // MachineDuck
    jun_money -= quantity * MachineDuck
    jun_stock += quantity

# 성민이
for idx, MachineDuck in enumerate(MachineDucks):
    if idx >= 3:
        # 매도시점
        if MachineDucks[idx - 3] < MachineDucks[idx - 2] < MachineDucks[idx - 1] < MachineDucks[idx]:
            sung_money += MachineDucks[idx] * sung_stock
            sung_stock = 0
        # 매수시점
        if MachineDucks[idx - 3] > MachineDucks[idx - 2] > MachineDucks[idx - 1] > MachineDucks[idx]:
            quantity = sung_money // MachineDuck
            sung_money -= quantity * MachineDuck
            sung_stock += quantity

jun_res = jun_money + MachineDucks[13] * jun_stock
sung_res = sung_money + MachineDucks[13] * sung_stock
print("SAMESAME") if jun_res == sung_res else print("BNP") if jun_res > sung_res else print("TIMING")