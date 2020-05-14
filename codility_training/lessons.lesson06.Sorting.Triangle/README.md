## 출처

https://app.codility.com/programmers/lessons/6-sorting/triangle/


## 번역
```text
N 개의 정수로 구성된 배열 A가 제공됩니다. 삼중 항 (P, Q, R)은 0 ≤ P <Q <R <N이고 다음과 같은 경우 삼각형입니다 .

A [P] + A [Q]> A [R],
A [Q] + A [R]> A [P],
A [R] + A [P]> A [Q].
예를 들어 다음과 같은 배열 A를 고려하십시오.

  A [0] = 10 A [1] = 2 A [2] = 5
  A [3] = 1 A [4] = 8 A [5] = 20
삼중 항 (0, 2, 4)은 삼각형입니다.

함수를 작성하십시오.

기능 솔루션 (A);

즉, N 정수로 구성된 배열 A가 주어지면이 배열에 삼각 삼중 항이 있으면 1을 반환하고 그렇지 않으면 0을 반환합니다.

예를 들어, 다음과 같은 배열 A가 제공됩니다.

  A [0] = 10 A [1] = 2 A [2] = 5
  A [3] = 1 A [4] = 8 A [5] = 20
위에서 설명한대로 함수는 1을 반환해야합니다. 주어진 배열 A는 다음과 같습니다.

  A [0] = 10 A [1] = 50 A [2] = 5
  A [3] = 1
함수는 0을 반환해야합니다.

다음 가정을위한 효율적인 알고리즘을 작성하십시오 .

N은 [ 0 .. 100,000 ] 범위 내의 정수 이며;
배열 A의 각 요소는 [ -2,147,483,648 .. 2,147,483,647 ] 범위 내의 정수 이다.

```

## 원문
```text
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

function solution(A);

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

```
=======

