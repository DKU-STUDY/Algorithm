class Solution {
    class UnionFind(size:Int){
        val root:IntArray by lazy { IntArray(size){it} }


        fun union(x:Int, y:Int):Boolean{
            val rootX = find(x)
            val rootY = find(y)
            if(rootX!=rootY){
                when{
                    rootX>rootY -> root[rootX] = rootY
                    rootX<rootY -> root[rootY] = rootX
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
    fun smallestEquivalentString(s1: String, s2: String, baseStr: String): String {
        val n = s1.length
        val unionfind = UnionFind(26)
        for(i in 0..n-1){
            unionfind.union(s1[i]-'a', s2[i]-'a')
        }
        var res = ""
        for(i in baseStr.indices){
            val num = unionfind.find(baseStr[i]-'a')
            res += (num+'a'.toInt()).toChar()
        }
        return res
    }
}