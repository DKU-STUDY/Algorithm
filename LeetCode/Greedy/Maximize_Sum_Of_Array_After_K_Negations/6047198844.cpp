class Solution {
public:
    int largestSumAfterKNegations(vector<int>& A, int K) {
        sort(A.begin(),A.end());
        
        int res = 0;
        for(int i = 0 ; i < A.size(); i++){
            if(K){
                if(A[i]<0){
                    A[i] = -A[i];
                    K--;
                }else{
                    if(K%2){
                        if(i==0||A[i-1]>A[i]){
                            A[i] = -A[i];
                        }else{
                            res += -A[i-1]*2;
                        }
                    }
                    K=0;
                }
            }
            res += A[i];
        }
        
        return res;
    }
};