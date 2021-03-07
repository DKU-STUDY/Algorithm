package Fair_Candy_Swap;

class HyeonJeong {
    public int[] fairCandySwap(int[] A, int[] B) {
        int sumA = 0, sumB = 0;
        int [] result = new int[2];
        for (int a : A) {
            sumA += a;
        }
        for (int b : B) {
            sumB += b;
        }
        for (int j = 0; j < A.length; j++) {
            for (int i = 0; i < B.length; i++) {
                if (sumA + 2*B[i] == sumB + 2*A[j]) { // 값의 변경 후 합이 같은지
                    result[0] = A[j];
                    result[1] = B[i];
                    break;
                }
            }
        }
        return result;
    }
}
