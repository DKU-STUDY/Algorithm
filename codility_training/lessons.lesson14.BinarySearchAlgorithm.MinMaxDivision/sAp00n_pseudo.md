> 원문  

You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The *large sum* is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:

```
A[0] = 2
A[1] = 1
A[2] = 5
A[3] = 1
A[4] = 2
A[5] = 2
A[6] = 2
```

The array can be divided, for example, into the following blocks:

> - [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
> - [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
> - [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
> - [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.

The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

> ```
> def solution(K, M, A)
> ```

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:

```
A[0] = 2
A[1] = 1
A[2] = 5
A[3] = 1
A[4] = 2
A[5] = 2
A[6] = 2
```

the function should return 6, as explained above.

Write an ***\*efficient\**** algorithm for the following assumptions:

> - N and K are integers within the range [1..100,000];
> - M is an integer within the range [0..10,000];
> - each element of array A is an integer within the range [0..M].



> 번역

정수 K, M 및 N 정수로 구성된 비어 있지 않은 배열 A가 제공됩니다. 배열의 모든 요소는 M보다 크지 않습니다.

이 배열을 연속 된 요소의 K 블록으로 나누어야합니다. 블록의 크기는 0과 N 사이의 정수입니다. 배열의 모든 요소는 일부 블록에 속해야합니다.

X에서 Y까지의 블록의 합은 A [X] + A [X + 1] + ... + A [Y]와 같습니다. 빈 블록의 합은 0과 같습니다.

큰 합은 모든 블록의 최대 합입니다.

예를 들어 정수 K = 3, M = 5 및 배열 A가 다음과 같이 주어집니다.
```
A [0] = 2
A [1] = 1
A [2] = 5
A [3] = 1
A [4] = 2
A [5] = 2
A [6] = 2
```
예를 들어 배열을 다음 블록으로 나눌 수 있습니다.

>- [2, 1, 5, 1, 2, 2, 2], [], []의 합이 15이고;
>- 큰 합이 9 인 [2], [1, 5, 1, 2], [2, 2];
>- [2, 1, 5], [], [1, 2, 2, 2]의 합이 8이고;
>- [2, 1], [5, 1], [2, 2, 2]의 합이 6입니다.
>- 목표는 큰 금액을 최소화하는 것입니다. 위의 예에서 6은 최소 큰 합입니다.

함수를 작성하십시오.

>- 데프 솔루션 (K, M, A)

즉, 정수 K, M 및 N 정수로 구성된 비어 있지 않은 배열 A가 주어지면 최소 큰 합을 반환합니다.

예를 들어, K = 3, M = 5 및 배열 A는 다음과 같습니다.

```
A [0] = 2	
A [1] = 1	
A [2] = 5	
A [3] = 1	
A [4] = 2	
A [5] = 2	
A [6] = 2
```
위에서 설명한 것처럼 함수는 6을 반환해야합니다.

다음 가정을위한 ***효율적인*** 알고리즘을 작성하십시오.

>- N 및 K는 [1..100,000] 범위 내의 정수이며;
>- M은 [0..10,000] 범위 내의 정수이며;
>- 배열 A의 각 요소는 [0..M] 범위 내의 정수입니다.



> Pseudo code 

* 목표

>-min_Max_division 구하기

* 이진탐색 이용

  * 1. 예상값(low, middle, high)지정

    2. 다중loop 돌려 예상값이 최적해에 부합하는지 검사.

       2-1. 맞다면 값 리턴

       2-2. 아니면 예상값을 이진탐색으로 범위 수정.