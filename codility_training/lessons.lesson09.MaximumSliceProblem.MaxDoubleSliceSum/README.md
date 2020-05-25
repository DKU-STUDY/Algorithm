# Maximum slice problem
https://codility.com/media/train/7-MaxSlice.pdf

## 문제
https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/

## 문제 설명
https://hwan-shell.tistory.com/124

## 번역
```text
N 개의 정수로 구성된 비어 있지 않은 배열 A가 제공됩니다.

0≤X <Y <Z <N이되도록 삼중 항 (X, Y, Z)을 더블 슬라이스 라고합니다 .

합 + A [Y + 1] + A [- 이중 슬라이스 (X, Y, Z)의이 A [X + 1] + A [X + 2] + ... + A [1 Y]의 합계이며 Y + 2] + ... + A [Z-1].

예를 들어, 배열 A는 다음과 같습니다.

    A [0] = 3
    A [1] = 2
    A [2] = 6
    A [3] = -1
    A [4] = 4
    A [5] = 5
    A [6] = -1
    A [7] = 2
다음 예제 더블 슬라이스를 포함합니다.

더블 슬라이스 (0, 3, 6), 합계는 2 + 6 + 4 + 5 = 17입니다.
더블 슬라이스 (0, 3, 7), 합계는 2 + 6 + 4 + 5-1 = 16입니다.
더블 슬라이스 (3, 4, 5)에서 합계는 0입니다.
목표는 더블 슬라이스의 최대 합을 찾는 것입니다.

함수를 작성하십시오.

클래스 솔루션 {public int solution (int [] A); }

N 개의 정수로 구성된 비어 있지 않은 배열 A가 주어지면 더블 슬라이스의 최대 합을 반환합니다.

예를 들면 다음과 같습니다.

    A [0] = 3
    A [1] = 2
    A [2] = 6
    A [3] = -1
    A [4] = 4
    A [5] = 5
    A [6] = -1
    A [7] = 2
배열 A의 이중 슬라이스의 합이 17보다 크지 않으므로 함수는 17을 반환해야합니다.

다음 가정을위한 효율적인 알고리즘을 작성하십시오 .

N은 [ 3 .. 100,000 ] 범위의 정수 이며;
배열 A의 각 요소는 [ -10,000 .. 10,000 ] 범위 내의 정수 입니다.
```

## 원문
```text
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
```