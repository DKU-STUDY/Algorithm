# 출처

https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

function solution(A); 이고 배열의 크기가 4 이라면. 요소들의 특징은. 1~5 숫자중 한 숫자만 빠져있다. 빠져있는 숫자를 리턴하라
```
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
```

```
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
```
