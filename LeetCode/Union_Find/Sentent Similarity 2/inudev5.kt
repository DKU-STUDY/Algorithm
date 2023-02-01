class Solution {
    class UnionFind(sentence:List<List<String>>){

        val root:HashMap<String, String> by lazy {
            val map =hashMapOf<String,String>()
            for((a,b) in sentence){map.putIfAbsent(a,a);map.putIfAbsent(b,b)}
            map
        }
        val rank:HashMap<String, Int> by lazy {
            val map =hashMapOf<String, Int>()
            root.keys.forEach{key-> map.put(key,1)}
            map
        }

        //node가 String인 경우


        fun union(x:String, y:String):Boolean{
            val rootX = find(x)
            val rootY = find(y)
            if(rootX!=rootY){
                when{
                    rank[rootX]!!>rank[rootY]!! -> root[rootY] = rootX
                    rank[rootX]!!<rank[rootY]!! -> root[rootX] = rootY
                    else->{
                        root[rootX] = rootY
                        rank.put(rootY, rank.getOrDefault(rootY,1)+1)
                    }
                }
                return true
            }
            return false
        }
        fun find(word:String):String{
            if(word==root[word])return word
            root[word] = find(root.getValue(word))
            return root.getValue(word)
        }
    }
    fun areSentencesSimilarTwo(sentence1: Array<String>, sentence2: Array<String>, similarPairs: List<List<String>>): Boolean {
        if(sentence1.size!=sentence2.size)return false
        val unionfind = UnionFind(similarPairs)
        for((a,b) in similarPairs)unionfind.union(a,b)
        for(i in sentence1.indices){
            if(sentence1[i]==sentence2[i])continue
            if(unionfind.root[sentence1[i]]==null ||unionfind.root[sentence2[i]]==null) return false
            if(unionfind.find(sentence1[i])!=unionfind.find(sentence2[i]))return false
        }
        return true
    }
}