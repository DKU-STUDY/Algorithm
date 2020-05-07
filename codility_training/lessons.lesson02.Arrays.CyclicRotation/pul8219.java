package lessons.lesson02.Arrays.CyclicRotation;

class Solution{
    public int[] solution(int[] A, int K){
        int arr_len = A.length; // 배열 A의 크기 구하기
        int[] result = new int[arr_len]; // A배열과 같은 크기의 배열 생성

        if(K == arr_len) // 배열의 크기와 회전수 K가 같은 값이라면
            return A; // 배열 A를 그대로 리턴(회전해도 똑같으니까)

        for(int i = 0; i < arr_len; i++){
            result[(i + K) % arr_len] = A[i]; // (배열의 인덱스 + K) % 배열 A 길이 를 새로운 인덱스로 활용
        }

        return result;
    }
}

public class pul8219 {
    public static void main(String[] args){
        Solution s = new Solution();
        int[] A = {3,8,9,7,6};
        int K = 3;
        int[] result = s.solution(A, K);
        for(int i = 0; i < result.length; i++){
            System.out.printf("%d ", result[i]);
        }

    }
}
