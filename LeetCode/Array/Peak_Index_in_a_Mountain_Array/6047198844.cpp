class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int begin = 0;
        int end = arr.size()-1;
        while(begin < end){
            int mid = begin - (begin - end) / 2;
            
            if(arr[mid-1]<arr[mid]){
                begin = mid;
            }else{
                end = mid-1;
            }
        }
        return begin;
    }
};