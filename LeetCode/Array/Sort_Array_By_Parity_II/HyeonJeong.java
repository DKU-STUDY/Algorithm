package LeetCode.Array.Sort_Array_By_Parity_II;

class HyeonJeong {
    public int[] sortArrayByParityII(int[] A) {
        // A의 길이가 2의 배수이고, 항상 반환이 가능하다는 조건
        int odd = 0, even = 0, len = A.length;
        int []result = new int[len];
        for (int i = 0; i < len; i++) {
            if (A[i]%2 == 0) {
                result[2*even] = A[i];
                even++;
            }
            else {
                result[2*odd+1] = A[i];
                odd++;
            }
        }
        return result;
    }
}
