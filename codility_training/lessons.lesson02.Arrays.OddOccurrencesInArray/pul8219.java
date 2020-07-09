import java.util.HashSet;
import java.util.Set;

// 반복문으로 생각하다가 어떻게 풀어야될지 감이 안 잡혀서 솔루션 참고함
// HashSet, Iterator 사용에 미숙함. Java 공부 더더더---- 필요

class Solution{
    /* Solution 1 */
    public int solution(int[] A){
        int tmp = 0;
        for(int i = 0, len = A.length; i < len; i++ ){
            tmp = tmp ^ A[i]; //tmp 변수와 A[i] XOR 연산
        }
        return tmp;
    } // end of solution()

    /* Solution 2 */
    // HashSet 이용
    public int solution2(int[] A){
        // HashSet은 중복된 요소를 저장하지 않음
        Set<Integer> set = new HashSet<>();
        for(int i : A) {
            if (set.contains(i)) { //set에 i가 있다면
                set.remove(i); //set에서 삭제
            } else { //없다면
                set.add(i); //set에 추가
            }
        }//end of for loop
        return set.iterator().next();
    }//end of solution2()

} // end of class Solution




public class pul8219 {
    public static void main(String[] args){
        int A[] = {9,3,9,7,9,7,9};
        Solution s = new Solution();
        System.out.println(s.solution2(A));
    }
} // end of class pul8219






/*
        int len = A.length;
        int unpair = 0;

        for(int i = 0; i < len; i++){
            if(A[i] ==  A[i + 2])
                continue;
            else{

                if(i + 2 < len)
                    continue;
                unpair = A[i];
                else
                    break;
            }

        } // end of for loop
 */