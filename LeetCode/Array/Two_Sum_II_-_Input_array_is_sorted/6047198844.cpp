class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int,int> umap;
        for(int i = 0; i < numbers.size(); i++){
            int dif = target - numbers[i];
            if(umap[numbers[i]]){
                return vector<int>({umap[numbers[i]],i+1});
            }
            umap[dif] = i+1;
        }
        return vector<int>();
    }
};
//해쉬 테이블