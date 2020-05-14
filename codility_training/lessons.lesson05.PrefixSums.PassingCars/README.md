[문제출처](https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/)


## 입출력
```javascript
function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    return 1
}
console.log(
  solution([0, 1, 0, 1, 1]) === 5
);
```

## 문제 설명
(값인 0인 요소의 인덱스, 값이 1인 요의 인덱스) 쌍의 경우의 수 구하기 
0 <= 값인 0인 요소의 인덱스 < 값이 1인 요의 인덱스 
쌍의 수가 1,000,000,000을 초과하면이 함수는 -1을 반환

```text
  A [0] = 0
  A [1] = 1
  A [2] = 0
  A [3] = 1
  A [4] = 1
(0, 1), (0, 3), (0, 4), (2, 3), (2, 4)
```
## 번역
```text
N 개의 정수로 구성된 비어 있지 않은 배열 A가 제공됩니다. 배열 A의 연속 요소는 도로의 연속 자동차를 나타냅니다.

배열 A에는 0 및 / 또는 1 만 포함됩니다.

0은 동쪽으로 여행하는 자동차를 나타냅니다.
1은 서쪽으로 여행하는 자동차를 나타냅니다.
목표는 지나가는 자동차를 세는 것입니다. P가 동쪽으로 여행하고 Q가 서쪽으로 여행 할 때 0 ≤ P <Q <N 인 한 쌍의 자동차 (P, Q)가 지나가고 있다고합니다.

예를 들어 다음과 같은 배열 A를 고려하십시오.

  A [0] = 0
  A [1] = 1
  A [2] = 0
  A [3] = 1
  A [4] = 1
(0, 1), (0, 3), (0, 4), (2, 3), (2, 4)의 5 쌍의 통과 차량이 있습니다.

함수를 작성하십시오.

기능 솔루션 (A);

비어 있지 않은 배열 A의 N 정수가 주어지면 통과하는 자동차 쌍의 수를 반환합니다.

통과하는 차량 쌍의 수가 1,000,000,000을 초과하면이 함수는 -1을 반환해야합니다.

예를 들면 다음과 같습니다.

  A [0] = 0
  A [1] = 1
  A [2] = 0
  A [3] = 1
  A [4] = 1
위에서 설명한대로 함수는 5를 반환해야합니다.

다음 가정을위한 효율적인 알고리즘을 작성하십시오 .

N은 [ 1 .. 100,000 ] 범위의 정수 이며;
배열 A의 각 요소는 다음 값 중 하나를 가질 수있는 정수입니다. 0, 1
```


## 원문
```text
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
```
