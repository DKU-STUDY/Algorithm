class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        if(m*k > bloomDay.size())
            return -1;
        
        vector<int> Days = bloomDay;
        sort(Days.begin(),Days.end());
        Days.erase(unique(Days.begin(),Days.end()),Days.end());
        //Days에서 이분 탐색으로 고른다.
        int beginDay = 0;
        int endDay = Days.size()-1;
        while(beginDay < endDay){
            int midDay = (beginDay + endDay) / 2;
            int bouquetsN = 0;
            int bloomN = 0;
            for(int i = 0; i < bloomDay.size(); i++){
                if(bloomDay[i] <= Days[midDay]){
                    bloomN++;
                    if(bloomN == k){
                        bouquetsN++;
                        bloomN = 0;
                    }
                }else{
                    bloomN = 0;
                }
            }
            //주어진 날짜로 못만들었을때 -> 날짜를 늘려야한다.
            if(bouquetsN < m)
                beginDay = midDay + 1;
            //주어진 날짜로 만들었을때 -> 날짜를 줄인다.
            else
                endDay = midDay;
        }    
        return Days[beginDay];
    }
};
//100000 * lgN 1000
//100000000
//범위의 개념