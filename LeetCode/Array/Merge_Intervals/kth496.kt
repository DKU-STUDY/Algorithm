class Solution {
    fun merge(intervals: Array<IntArray>): Array<IntArray> {
        val answer: MutableList<IntArray> = ArrayList();
        intervals.sortWith(compareBy { it[0] })

        var temp: IntArray = intervals[0]
        for (i in 1 until intervals.size) {
            if (temp[1] >= intervals[i][0]) {
                temp[1] = temp[1].coerceAtLeast(intervals[i][1])
            } else {
                answer.add(temp)
                temp = intervals[i]
            }
        }
        answer.add(temp)

        return answer.toTypedArray()
    }
}