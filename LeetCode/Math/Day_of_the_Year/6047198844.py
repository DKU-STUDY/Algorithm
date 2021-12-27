class Solution:
    def dayOfYear(self, date: str) -> int:
        day = datetime.date.fromisoformat(date)
        return int(day.strftime('%j'))