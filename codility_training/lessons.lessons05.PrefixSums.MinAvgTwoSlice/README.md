[링크](https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/)
* 참고 https://www.youtube.com/watch?v=w0eFQwiKY7k

## 문제설명 
* 입출력 함수
  ```
  function solution(A) {
    return 0
  }
  console.log(solution([4, 2, 2, 5, 1, 5, 8]) === 1);
  ```

* 아이디어
  ```
   (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).
  ```
  
* 예시

  주어진 배열입니다. 
   ```
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
   ```
   
   slice 메서드를 실행했을 때. 배열 내에서 임의의 인덱스의 시작과 끝을 정합니다. 그리고 slice된 배열의 요소의 평균값을 구합니다.
   단, 0 ≤ 시작인덱스 < 끝인덱스 입니다.

  ```
  slice (1, 2), whose average is (2 + 2) / 2 = 2;
  slice (3, 4), whose average is (5 + 1) / 2 = 3;
  slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5
  ```
 
 이중 평균이 가장 작을 때의 시작 값을 반환하면 됩니다.

## 원문
```
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
```
