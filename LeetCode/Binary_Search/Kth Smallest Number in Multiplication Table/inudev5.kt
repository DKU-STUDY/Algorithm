class Solution {
    fun findKthNumber(m: Int, n: Int, k: Int): Int {
        //k번째 작은수
        // mat[i][j] = (i+1)*(j+1)
        var l = 1
        var r = m*n
        fun count(x:Int,k:Int):Boolean{ //if x has k or more values less than it
            var count=0
            for(i in 1..m)count+= minOf(x/i,n) //col에서 가능한 count
            return count>=k
        }
        while(l<r){
            val mid = l+(r-l)/2
            if(count(mid,k)) r=mid
            else l=mid+1
        }
        return l

    }
}