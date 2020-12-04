class Solution:
    def dayOfYear(self, date: str) -> int:
        mlist = [31,28,31,30,31,30,31,31,30,31,30,31]
        year, month, day = map(int, dat.split('-')
        # year = int(date[0:4])
        # month = int(date[5:7])
        # day = int(date[8:10])
        if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
            mlist[1] = 29
        answer = 0
        for i in range(month-1):
            answer += mlist[i]
        return answer + day
