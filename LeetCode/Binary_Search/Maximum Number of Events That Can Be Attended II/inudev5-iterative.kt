class Solution {
    fun maxValue(events: Array<IntArray>, k: Int): Int {

        events.sortBy{it[0]}//시작일,종료일로 정렬
        val n = events.size
        // val lastDay=events[n-1][1]
        val dp = Array(n+1){IntArray(k+1)}
        fun upperBound(events:Array<IntArray>, start:Int, target:Int):Int{
            var l=start
            var r= events.size
            while(l<r){
                val mid = l+(r-l)/2
                if(events[mid][0]<=target)l=mid+1
                else r=mid
            }
            return r
        }
        for(i in n-1 downTo 0){
            val next = upperBound(events,i+1,events[i][1])
            for(j in 1..k)dp[i][j] = maxOf(dp[i+1][j], events[i][2]+dp[next][j-1])
        }
        return dp[0][k]
    }
}