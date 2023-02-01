class Solution {
    //solution using binary search
    fun shortestDistanceColor(colors: IntArray, queries: Array<IntArray>): List<Int> {
        val map = hashMapOf<Int,MutableList<Int>>()
        for(i in colors.indices){
            map.putIfAbsent(colors[i], mutableListOf<Int>())
            map[colors[i]]!!.add(i)
        }
        val res = mutableListOf<Int>()
        fun lowerBound(arr:MutableList<Int>, target:Int):Int{
            var l=0
            var r=arr.size
            while(l<r){
                val mid= l+(r-l)/2
                when{
                    arr[mid]>=target -> r=mid
                    else -> l=mid+1
                }
            }
            return l
        }
        for((idx,color) in queries){
            if(color !in map){res.add(-1);continue}
            val idxList = map[color]!!
            val pos = lowerBound(idxList,idx) //idx 이상인 최소 인덱스
            when{
                pos==idxList.size -> res.add(idx-idxList[idxList.lastIndex])
                pos==0 -> res.add(idxList[0]-idx)
                else-> {
                    val left = idx-idxList[pos-1]
                    val right = idxList[pos]-idx
                    res.add(minOf(left,right))
                }
            }
        }

        return res
    }
}