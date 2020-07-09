https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

```
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized 
```

permutation 한지 묻는 문제입니다. true 이면 1 false 이면 0 을 반환하면됩니다.
만약 배열의 길이가 4일때, 요소가 1 ~ 4 를 가지고 있다면 1을 반환하고
배열길이가 3일 때는 1~3 을가지고 있어야 한다. 그 외 요소를 가지고 있거나 가지고 있지 않다면 0을 반환합니다
