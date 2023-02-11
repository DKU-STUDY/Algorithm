class Solution {
    class UnionFind(size:Int){
        val root:IntArray by lazy { IntArray(size){it} }
        val rank:IntArray by lazy { IntArray(size){1} }

        fun union(x:Int, y:Int):Boolean{
            val rootX = find(x)
            val rootY = find(y)
            if(rootX!=rootY){
                when{
                    rank[rootX]>rank[rootY] -> root[rootY] = rootX
                    rank[rootX]<rank[rootY]-> root[rootX]= rootY
                    else->{
                        root[rootY]= rootX
                        rank[rootX]+=1
                    }
                }
                return true
            }
            return false
        }
        fun find(x:Int):Int{
            if(x==root[x])return x
            root[x] = find(root[x])
            return root[x]
        }
    }
    fun earliestAcq(logs: Array<IntArray>, n: Int): Int {
        val uf=UnionFind(n)
        var prestamp = 0
        var count=n
        logs.sortBy({it[0]})
        for((timestamp,a,b) in logs){
            if(uf.union(a,b))count-=1
            if(count==1)return timestamp
        }
        return -1
    }
}