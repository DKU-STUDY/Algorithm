https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

* good lecture https://www.youtube.com/watch?v=scD312I7kkE
```
Write a function:

class Solution { public int solution(int A, int B, int K); }

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
```

정수 인수 , A, B ,K 가 주어지고, A <= B 입니다.  이 범위 사이의 수 중 (A<= i <= B) 가 K로 나누었을 때 나머지가 0이 되는 수의 갯수를 return 하는 문제입니다.
