## [Sorting](https://codility.com/media/train/4-Sorting.pdf)

[문제출처](https://app.codility.com/programmers/lessons/6-sorting/distinct/)

## 번역
```text
N 개의 정수로 구성된 배열 A가 주어지면 배열 A의 고유 값 수를 반환합니다.

예를 들어, 배열 A는 다음과 같은 6 가지 요소로 구성됩니다.

 A [0] = 2 A [1] = 1 A [2] = 1
 A [3] = 2 A [4] = 3 A [5] = 1
이 함수는 배열 A에 3, 즉 1, 2 및 3으로 구분되는 3 개의 고유 한 값이 있기 때문에 3을 반환해야합니다.

다음 가정을위한 효율적인 알고리즘을 작성하십시오 .

N은 [ 0 .. 100,000 ] 범위 내의 정수 이며;
배열 A의 각 요소는 [ -1,000,000 .. 1,000,000 ] 범위의 정수 입니다.
```
## 원문
```text
Write a function

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
```