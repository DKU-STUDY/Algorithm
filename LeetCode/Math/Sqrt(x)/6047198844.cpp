class Solution {
public:
    int mySqrt(int x) {
        if(x==0)
            return 0;
        
        long long begin = 1;
        long long end = (long long)x+1;
        int ans = 0;
        while(begin <end){
            long long mid = (begin + end) / 2;
            
            if(mid*mid <= x){
                begin = mid + 1;
                ans = mid;
            }
            else
                end = mid;
        }
        
        return ans;
    }
};