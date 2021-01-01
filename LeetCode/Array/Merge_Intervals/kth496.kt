class Solution {
    fun merge(intervals: Array<IntArray>): Array<IntArray?> {
        val answer: MutableList<IntArray?> = ArrayList();
        intervals.sortWith(compareBy { it[0] })

        var temp: IntArray? = null
        for (interval in intervals) {
            when {
                temp == null -> temp = interval
                temp[1] >= interval[0] -> temp[1] = max(temp[1], interval[1])
                else -> {
                    answer.add(temp)
                    temp = interval
                }
            }
        }
        answer.add(temp)

        return answer.toTypedArray()
    }
}