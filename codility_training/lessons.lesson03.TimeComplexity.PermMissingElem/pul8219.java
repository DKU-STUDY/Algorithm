package lessons.lesson03.TimeComplexity.PermMissingElem;

// 배열 A -> N개의 서로 다른 숫자
// 1 ~ N+1 의 정수를 포함, 한 가지 요소가 빠져있음
// 배열에서 빠진 요소를 리턴하는 함수 작성하기

import java.util.Arrays;

class Solution{
    public int solution(int[] A){
        Arrays.sort(A); // 배열 A를 오름차순으로 정렬

        for(int i = 0, len = A.length; i < len; i++){ // 배열 크기 만큼 반복
            if(i+1 != A[i]) // 배열 A는 오름차순으로 정렬되어있으므로 i를 증가시켜가며 값이 달라지는 때
                return i+1; // missing된 값을 리턴
        }

        // 가장 큰 값이 missing 됐을 경우는 위의 for문에서 파악할 수 없으므로 따로 고려해줘야함
        return A.length + 1;

    }
}


public class pul8219 {
    public static void main(String[] args){
        int[] A = {3,2,1,4,5};
        Solution s = new Solution();
        System.out.println(s.solution(A));

    }
}
