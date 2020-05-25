# MaximumSliceProblem - MaxSliceSum

## 출처

https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/

## 원문

```
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
```

## 번역

```
N 정수로 구성된 비어 있지 않은 배열 A가 주어진다.
0 ≤ P ≤ Q < N과 같은 정수(P, Q) 한 쌍을 배열 A의 슬라이스라고 한다. 
슬라이스(P, Q)의 합은 A[P] + A[P+1] + ...의 합이다. + A[Q]

함수 작성

def solution(A)

N 정수로 구성된 배열 A가 주어진 경우, A 조각의 최대 합계를 반환한다.

예를 들어, 다음과 같은 배열 A가 주어진 경우:

A[0] = 3 A[1] = 2 A[2] = -6
A[3] = 4 A[4] = 0
다음과 같은 이유로 함수는 5를 반환해야 한다.

(3, 4)는 A의 한 조각으로, 합이 4이고,
(2, 2)는 A의 한 조각으로, 합이 -6이고,
(0, 1)는 A의 한 조각으로, 합이 5이고,
A의 다른 절편에는 (0, 1)보다 큰 합이 없다.
다음과 같은 가정에 대해 효율적인 알고리즘을 작성한다.

N은 [1..1000,000] 범위 내의 정수;
배열 A의 각 요소는 [-1,000,000..1,000,000,000] 범위 내의 정수임;
결과는 [-2,12,483,648..2,164,483,647] 범위 내의 정수가 될 것이다.
```