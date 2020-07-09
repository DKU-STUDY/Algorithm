[문제출처](https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/)

## 입출력
```javascript
function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    return 1
}
console.log(solution([-3, 1, 2, -2, 5, 6]) === 60);
```

## 번역
```text
N 개의 정수로 구성된 비어 있지 않은 배열 A가 제공됩니다. 삼중 항 (P, Q, R) 의 곱은 A [P] * A [Q] * A [R] (0 ≤ P <Q <R <N)과 같습니다.

예를 들어, 배열 A는 다음과 같습니다.

  A [0] = -3
  A [1] = 1
  A [2] = 2
  A [3] = -2
  A [4] = 5
  A [5] = 6
다음과 같은 세 가지 예제가 들어 있습니다.

(0, 1, 2), 곱은 −3 * 1 * 2 = −6입니다.
(1, 2, 4), 제품은 1 * 2 * 5 = 10
(2, 4, 5), 제품은 2 * 5 * 6 = 60
당신의 목표는 삼중 항의 최대 제품을 찾는 것입니다.

함수를 작성하십시오.

클래스 솔루션 {public int solution (int [] A); }

비어 있지 않은 배열 A가 주어지면 삼중 항의 최대 곱의 값을 반환합니다.

예를 들어, 다음과 같은 배열 A가 제공됩니다.

  A [0] = -3
  A [1] = 1
  A [2] = 2
  A [3] = -2
  A [4] = 5
  A [5] = 6
삼중 항 (2, 4, 5)의 곱이 최대이므로 함수는 60을 반환해야합니다.

다음 가정을위한 효율적인 알고리즘을 작성하십시오 .

N은 [ 3 .. 100,000 ] 범위의 정수 이며;
배열 A의 각 요소는 [ -1,000 .. 1,000 ] 범위의 정수 입니다.
```
## 원문
```text
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
```