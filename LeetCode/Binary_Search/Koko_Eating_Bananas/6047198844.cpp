class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int start = 1;
        int end = *max_element(piles.begin(),piles.end());
        
        while(start < end){
            int sum = 0;
            int mid = (start + end ) / 2;
            for(int pile : piles)  
                sum += (pile + mid - 1) / mid;
            if(sum > h)
                start = mid + 1;
            else
                end = mid;
        }        
        return start;
    }
};