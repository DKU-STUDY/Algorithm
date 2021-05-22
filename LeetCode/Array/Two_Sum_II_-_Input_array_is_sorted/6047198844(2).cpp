class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size()-1;
        int sum;
        while((sum=numbers[l]+numbers[r])!=target){
            if(sum < target){
                l++;
            }else{
                r--;
            }
        }
        vector<int> res;
        res.push_back(l+1);
        res.push_back(r+1);
        return res;
    }
};
//투포인터
