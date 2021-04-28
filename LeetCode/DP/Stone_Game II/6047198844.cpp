class Solution {
private:
    int memo[100][100];
    
public:
    int dp(vector<int>& presum, int p , int m){
        if(presum.size() - p <= 2 * m) // presum.size() - p : 남은 숫자의 수 / 2 * m 최대 뽑을수있는 숫자의 수
            return presum[p];
        
        int &res = memo[p][m];
        if(res)
            return res;
        
        for(int x = 1; x <= 2*m; x++){
            int s = presum[p] - presum[p+x];
            res = max(res, s + (presum[p+x] - dp(presum, p+x, max(m,x))));
        }
        
        return res;
    }
    
    int stoneGameII(vector<int>& piles) {
        vector<int> presum = piles;
        for(int i = piles.size()-2; i >= 0; i--)
            presum[i] += presum[i+1];
        memset(memo,0,sizeof(memo));
        
        return dp(presum,0,1);
    }
};

//presum을 이용한다.
//memo를 제대로 이용한다.
