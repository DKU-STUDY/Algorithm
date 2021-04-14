class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        int res = 0;
        Queue<String> queue = new LinkedList<String>();
        HashSet<String> check = new HashSet<String>();

        queue.add(beginWord);
        check.add(beginWord);
        
        while(!queue.isEmpty()){
            res++;
            int Qsize = queue.size();
            while(Qsize!=0){
            	Qsize--;
                String curWord = queue.poll();
                if(endWord.equals(curWord))
                    return res;
                
                for(String w : wordList){
                    if(!check.contains(w)){
                        int cnt = 0;
                        for(int i = 0; i < w.length() && cnt <= 1; i++){
                            if(w.charAt(i) != curWord.charAt(i))
                                cnt++;
                        }
                        if(cnt == 1){
                            queue.add(w);
                            check.add(w);
                        }
                    }
                }
            }
        }
        return 0;
    }
}