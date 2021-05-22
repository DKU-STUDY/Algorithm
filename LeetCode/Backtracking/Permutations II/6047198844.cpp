class Solution {
private:
    vector<vector<int>> res;
public:
    void makePermutation(vector<int> &temp,vector<int> &pickCheck, const vector<int>& nums){
        //다뽑은 경우의수
        if(temp.size()==nums.size()){
            res.push_back(temp);
            return;
        }
        
        //현재 뽑았던 수중에 중복되는 수는 뽑지 않는다.
        bool dupCheck[21];
        fill_n(dupCheck,21,false);

        //이미 뽑았던 인덱스(pickCheck)는 뽑지 않는다.
        //나머지는 뽑아도된다.
        for(int i = 0; i < nums.size(); i++){
            if(!dupCheck[nums[i]+10]&&!pickCheck[i]){
                dupCheck[nums[i]+10] = true;
                pickCheck[i] = 1;
                temp.push_back(nums[i]);
                makePermutation(temp, pickCheck, nums);
                temp.pop_back();
                pickCheck[i] = 0;
            }
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<int>temp;
        vector<int>pickCheck(nums.size(),0);
        makePermutation(temp,pickCheck, nums);
        return res;
    }
};