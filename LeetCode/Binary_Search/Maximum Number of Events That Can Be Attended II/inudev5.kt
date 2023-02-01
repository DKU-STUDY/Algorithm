class Solution {
    fun maxValue(events: Array<IntArray>, k: Int): Int {
        //(시작 ,종료,보상) 종료일+1부터 다음 이벤트
        //k개를 골랐을 때 maxSum
        // var r = events.sumOf{it[2]}
        events.sortBy{it[0]}//시작일로 정렬(이분탐색 대상이 시작일이기 때문)
        val n = events.size
        // val lastDay=events[n-1][1]
        val dp = Array(n+1){IntArray(k+1){-1}}
        fun upperBound(events:Array<IntArray>, start:Int, target:Int):Int{
            var l=start
            var r= events.size
            while(l<r){
                val mid = l+(r-l)/2 //l+(r-l+1)/2는 TLE가 난다. 2개 남았을 때를 생각하면됨
                if(events[mid][0]<=target)l=mid+1
                else r=mid
            }
            return r
        }
        fun solve(idx:Int, k:Int):Int{
            if(idx>=n || k==0)return 0
            if(dp[idx][k]!=-1)return dp[idx][k]
            val next = upperBound(events,idx+1,events[idx][1])
            dp[idx][k] = maxOf(solve(idx+1,k), events[idx][2]+solve(next,k-1))
            return dp[idx][k]
        }

        return solve(0,k)
    }
}