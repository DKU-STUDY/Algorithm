package LeetCode.Array.Flipping_an_Image;

class HyeonJeong {
    public int[][] flipAndInvertImage(int[][] A) {
        int len = A.length, tmp;
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len/2; j++) {
                tmp = A[i][j];
                A[i][j]= (A[i][len-(j+1)] == 1)?0:1;
                A[i][len-(j+1)] = (tmp == 1)?0:1;
            }
            if (len%2 == 1)
                A[i][len/2] = (A[i][len/2] == 1)?0:1;
        }
        return A;
    }
}
