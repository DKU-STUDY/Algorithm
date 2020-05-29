 번역
-
N 정수로 구성된 배열 A가 주어진다.

각 숫자 A[i]에 대해 0 ≤ i < N에 대해, A[i]의 약수가 아닌 배열의 요소 수를 세고자 한다. 우리는 이 원소들이 약수가 아니라고 말한다.

예시의 다음 N = 5 인 배열 A를 고려하십시오.

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
다음 원소의 경우:

    A[0] = 3, non-divisors: 2, 6,
    A[1] = 1, non-divisors: 3, 2, 3, 6,
    A[2] = 2, non-divisors: 3, 3, 6,
    A[3] = 3, non-divisors: 2, 6,
    A[4] = 6, non-divisors: 없다.

함수를 작성하시오:

def solution(A)

N개의 정수로 구성된 배열 A가 주어진 경우, non-약수의 양을 나타내는 일련의 정수를 반환한다.

결과 배열을 정수의 배열로 반환해야 한다.

예를 들어, 다음과 같다.

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
함수는 위에서 설명한 대로 [2, 4, 3, 2, 0]을 반환해야 한다.

다음과 같은 가정에 대해 효율적인 알고리즘을 작성하십시오.

N은 [1..50,000] 범위 내의 정수;
배열 A의 각 요소는 [1..] 범위 내의 정수다.2 * N]

원문
-
You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:
    
    A[0] = 3, the non-divisors are: 2, 6,
    A[1] = 1, the non-divisors are: 3, 2, 3, 6,
    A[2] = 2, the non-divisors are: 3, 3, 6,
    A[3] = 3, the non-divisors are: 2, 6,
    A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N].