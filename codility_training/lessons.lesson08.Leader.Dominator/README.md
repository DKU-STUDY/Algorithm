# Leader - Dominator

## About Leader 
http://blog.naver.com/PostView.nhn?blogId=1net1&logNo=221237882968

## 출처

https://app.codility.com/programmers/lessons/8-leader/dominator/

## 원문

```
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
```

## 번역

```
N 개의 정수로 구성된 배열 A가 제공됩니다. 배열 A의 지배자는 A 요소의 절반 이상에서 발생하는 값입니다.

예를 들어 배열 A를 고려하여

 A [0] = 3 A [1] = 4 A [2] = 3
 A [3] = 2 A [4] = 3 A [5] = -1
 A [6] = 3 A [7] = 3
A의 지배자는 A의 8 개 요소 중 5 개 (즉, 인덱스 0, 2, 4, 6 및 7을 가진 요소 중 5 개)에서 발생하고 5는 8의 절반 이상이기 때문에 3입니다.

함수 작성

클래스 솔루션 {public int solution (int [] A); }

즉, N 개의 정수로 구성된 배열 A가 주어지면 A의 지배자가 발생하는 배열 A의 모든 요소의 인덱스를 반환합니다. 배열 A에 지배자가 없으면 함수는 -1을 반환해야합니다.

예를 들어, 주어진 배열 A는

 A [0] = 3 A [1] = 4 A [2] = 3
 A [3] = 2 A [4] = 3 A [5] = -1
 A [6] = 3 A [7] = 3
함수는 위에서 설명한대로 0, 2, 4, 6 또는 7을 반환 할 수 있습니다.

다음 가정을위한 효율적인 알고리즘을 작성하십시오.

N은 [0..100,000] 범위 내의 정수이며;
배열 A의 각 요소는 [-2,147,483,648..2,147,483,647] 범위의 정수입니다.
```