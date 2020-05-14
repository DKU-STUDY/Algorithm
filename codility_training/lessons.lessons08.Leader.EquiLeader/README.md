# Leader - EquilLeader

## 출처 

https://app.codility.com/programmers/lessons/8-leader/

## 원문

```
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
```

## 번역

```
N 개의 정수로 구성된 비어 있지 않은 배열 A가 제공됩니다.

이 배열의 리더는 A 요소의 절반 이상에서 발생하는 값입니다.

등가 리더는 0 ≤ S <N-1이고 두 시퀀스 A [0], A [1], ..., A [S] 및 A [S + 1], A [S + 2 인 인덱스 S입니다. ], ..., A [N-1]은 같은 값의 리더를가집니다.

예를 들어, 다음과 같은 배열 A가 제공됩니다.

    A [0] = 4
    A [1] = 3
    A [2] = 4
    A [3] = 4
    A [4] = 4
    A [5] = 2
우리는 두 명의 평등 지도자를 찾을 수 있습니다 :

순서 : (4) 및 (3, 4, 4, 4, 2)는 동일한 리더를 가지므로 값은 4입니다.
(4, 3, 4) 및 (4, 4, 2)의 시퀀스는 동일한 리더를 가지므로 값은 4입니다.
목표는 평등 지도자의 수를 세는 것입니다.

함수를 작성하십시오.

클래스 솔루션 {public int solution (int [] A); }

즉, N 개의 정수로 구성된 비어 있지 않은 배열 A가 있으면 등가 리더의 수를 반환합니다.

예를 들면 다음과 같습니다.

    A [0] = 4
    A [1] = 3
    A [2] = 4
    A [3] = 4
    A [4] = 4
    A [5] = 2
위에서 설명한 것처럼 함수는 2를 반환해야합니다.

다음 가정을위한 효율적인 알고리즘을 작성하십시오.

N은 [1..100,000] 범위의 정수이며;
배열 A의 각 요소는 [-1,000,000,000..1,000,000,000] 범위의 정수입니다.```