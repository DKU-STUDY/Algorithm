class Solution {
    fun smallestDistancePair(nums: IntArray, k: Int): Int {
        //pick two regardlesss of order
        val n = nums.size

        fun count(dist:Int, k:Int):Boolean{ //using two pointer two count number of valid distances
            var (l,r,count) = listOf(0,0,0)
            while(l<n){
                while(r<n && nums[r]-nums[l]<=dist)r++
                count+= r-l-1
                l++
            }
            return count>=k
        }
        nums.sort()

        var l = 0
        var r = nums[n-1]-nums[0]

        while(l<r){
            val mid=l+(r-l)/2
            //k개 이상임
            if(count(mid,k)) r=mid
            else l=mid+1
        }
        return l
    }
}
