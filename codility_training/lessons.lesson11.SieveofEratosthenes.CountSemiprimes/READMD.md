## 출처
https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_semiprimes/

## 원문
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

class Solution { public int[] solution(int N, int[] P, int[] Q); }

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P, Q is an integer within the range [1..N];
P[i] ≤ Q[i].

## 설명
- 프라임 : 소수,  2, 3, 5, 7, 11 및 13
- 세미프라임 : 두개의 소수로 이뤄진 수,  4, 6, 9, 10, 14, 15, 21, 22, 25, 26

매개변수 N P Q가 주어질 때,
 1 ≤ P [K] ≤ Q [K] ≤ N. 이다.
 
 
 예를 들어 정수 N = 26 및 배열 P, Q 등을 고려하십시오.
 
     P[0] = 1    Q[0] = 26
     P[1] = 4    Q[1] = 10
     P[2] = 16   Q[2] = 20
     
 이러한 각 범위 내에서 세미프라임 수는 다음과 같습니다.
 
 (1, 26)은 10,
 (4, 10)은 4,
 (16, 20)은 0입니다.
 
 [10, 4, 0]을 반환
 
