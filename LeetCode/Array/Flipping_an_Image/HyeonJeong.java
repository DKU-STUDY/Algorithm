package LeetCode.Array.Flipping_an_Image;

class HyeonJeong {
    public int[][] flipAndInvertImage(int[][] A) {
        int len = A.length, tmp;
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len/2; j++) {
                // 각 행을 역순으로 정렬하고 이미지를 반전시킨 상태가 되도록 함
                tmp = A[i][j];
                A[i][j]= (A[i][len-(j+1)] == 1)?0:1;
                A[i][len-(j+1)] = (tmp == 1)?0:1;
            }
            if (len%2 == 1) // 배열의 행 길이가 홀수일 때, 가운데 숫자의 이미지를 반전시킴
                A[i][len/2] = (A[i][len/2] == 1)?0:1;
        }
        return A;
    }
}
