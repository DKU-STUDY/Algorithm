class Solution {
    fun merge(intervals: Array<IntArray>): Array<IntArray> {
        val answer: MutableList<IntArray> = ArrayList();
        intervals.sortWith(compareBy { it[0] })

        var temp: IntArray = intervals[0]
        for (interval in intervals) {
            if (temp[1] >= interval[0])
                temp[1] = temp[1].coerceAtLeast(interval[1])
            else {
                answer.add(temp)
                temp = interval
            }
        }
        answer.add(temp)

        return answer.toTypedArray()
    }
}