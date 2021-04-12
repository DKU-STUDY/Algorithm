class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        
        nums1.erase(unique(nums1.begin(),nums1.end()),nums1.end());
        nums2.erase(unique(nums2.begin(),nums2.end()),nums2.end());
        
        int i = 0;
        int j = 0;
        vector<int> res;
        while(i<nums1.size()&&j<nums2.size()){
            if(nums1[i]==nums2[j]){
                res.push_back(nums1[i]);
                i++;
                j++;
            }else if(nums1[i] > nums2[j]){
                j++;
            }else{
                i++;
            }
        }
        return res;
    }
};