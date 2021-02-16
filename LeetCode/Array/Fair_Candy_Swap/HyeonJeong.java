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
                if (sumA + 2*B[i] == sumB + 2*A[j]) { // 값이 변경된 경우에 두 사람의 캔디량이 같은지 확인
                    result[0] = A[j];
                    result[1] = B[i];
                    break;
                }
            }
        }
        return result;
    }
}
