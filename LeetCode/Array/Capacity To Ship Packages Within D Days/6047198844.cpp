class Solution {
public:
    int shipWithinDays(vector<int>& weights, int D) {
        int begin = *max_element(weights.begin(), weights.end());
        int end = accumulate(weights.begin(), weights.end(), 0);

        //Day가 크다. -> 용량을 늘린다.
        //Day가 작다. -> 용량을 줄인다.

        while (begin < end) {
            int capa = 0;
            int day = 1; //중요
            int mid = (begin + end) / 2;
            for (int i = 0; i < weights.size(); i++) {
                capa += weights[i];
                if (capa > mid) {
                    capa = weights[i];
                    day++;
                }
            }

            if (day <= D) {
                end = mid;
            }
            else {
                begin = mid + 1;
            }
        }

        return begin;
    }
};