import java.util.Arrays;

public class sjjyy {
    /*
        https://programmers.co.kr/learn/courses/30/lessons/12941
        @param A, B : 길이가 같은 자연수 배열
        배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱함. 배열의 길이만큼 반복.
        두 수를 곱한 값을 누적하여 더함.
        @return 누적된 값의 최솟값
    */
    public static int solution(int[] A, int[] B) {
        int answer = 0;

        Arrays.sort(A);
        Arrays.sort(B); // 배열 정렬

//        int j = B.length - 1;
//        for (int i : A) {
//            answer += i * B[j];
//            j--;
//        }

        int len = A.length;
        for (int i = 0 ; i < len ; i++) {
            answer += A[i] * B[len - 1 - i];
        } // 누적된 값의 최솟값은 한 배열의 최댓값 * 최솟값을 누적한 값이 최솟값이 됨

        return answer;
    }

    public static void main(String[] args) {
        int[] A1 = {1, 4, 2};
        int[] B1 = {5, 4, 4};
        int[] A2 = {1, 2};
        int[] B2 = {3, 4};
        System.out.println(solution(A1, B1)); // 29
        System.out.println(solution(A2, B2)); // 10
    }
}
