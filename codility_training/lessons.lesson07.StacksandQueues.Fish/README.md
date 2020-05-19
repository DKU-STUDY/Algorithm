## 출처
https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

## 입출력
```javascript
function solution(A, B) {
    // write your code in JavaScript (Node.js 8.9.4)
    return 0;
}

console.log(
  solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) === 2
)
```
## 문제설명
  solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) === 2

배열이 주어지면 첫번째 배열은 물고기의 크기 입니다. 두번째 배열은 물고기가 가는 방향이며 0 은 상류, 1은 하류 로 향합니다
서로 반대방향에서 마주치는 물고기중 큰 물고기가 살아남는다. 
리턴할 값은 살아남은 물고기의 수이다.  

## 번역
```text
N 개의 정수로 구성된 비어 있지 않은 두 개의 배열 A와 B가 제공됩니다. 배열 A와 B는 강의 흐름을 따라 하류로 정렬 된 강에서 N 개의 끔찍한 물고기를 나타냅니다.

물고기는 0에서 N-1까지 번호가 매겨집니다. P와 Q가 두 물고기이고 P <Q 인 경우, 물고기 P는 처음에 물고기 Q의 상류에 있습니다. 처음에는 각 물고기의 위치가 고유합니다.

물고기 번호 P는 A [P] 및 B [P]로 표시됩니다. 배열 A는 물고기의 크기를 포함합니다. 모든 요소는 독특합니다. 배열 B에는 물고기의 방향이 포함되어 있습니다. 여기에는 0 및 / 또는 1 만 포함됩니다.

0은 상류로 흐르는 물고기를 나타냅니다.
1은 하류로 흐르는 물고기를 나타냅니다.
두 물고기가 반대 방향으로 움직이고 그들 사이에 다른 (생존하는) 물고기가 없으면 결국 서로 만나게됩니다. 그러면 한 마리의 물고기 만 살 수 있습니다. 큰 물고기는 작은 물고기를 먹습니다. 보다 정확하게 말하면, P <Q, B [P] = 1 및 B [Q] = 0 일 때 두 물고기 P와 Q가 서로 만나고 그들 사이에 살아있는 물고기가 없다고 말합니다. 그들이 만나면 :

A [P]> A [Q] 인 경우 P는 Q를 먹고 P는 여전히 하류로 흐릅니다.
A [Q]> A [P]이면 Q는 P를 먹고 Q는 여전히 상류로 흐릅니다.
우리는 모든 물고기가 같은 속도로 흐르고 있다고 가정합니다. 즉, 같은 방향으로 움직이는 물고기는 절대 만나지 않습니다. 목표는 살아남을 물고기 수를 계산하는 것입니다.

예를 들어, 배열 A와 B를 다음과 같이 고려하십시오.

  A [0] = 4 B [0] = 0
  A [1] = 3 B [1] = 1
  A [2] = 2 B [2] = 0
  A [3] = 1 B [3] = 0
  A [4] = 5 B [4] = 0
처음에는 모든 물고기가 살아 있고 물고기 번호 1을 제외한 모든 물고기가 상류로 이동합니다. 물고기 번호 1은 물고기 번호 2를 만나서 먹은 다음 물고기 번호 3을 만나서 먹습니다. 마지막으로 물고기 4 번을 만나서 먹습니다. 숫자 0과 4의 나머지 두 물고기는 절대 만나지 않으므로 살아남습니다.

함수를 작성하십시오.

기능 솔루션 (A, B);

즉, N 개의 정수로 구성된 비어 있지 않은 두 개의 배열 A와 B가 제공되면 살아남을 물고기 수를 반환합니다.

예를 들어 위에 표시된 배열이 주어지면 함수는 위에서 설명한 것처럼 2를 반환해야합니다.

다음 가정을위한 효율적인 알고리즘을 작성하십시오 .

N은 [ 1 .. 100,000 ] 범위의 정수 이며;
어레이 A의 각 요소는 범위 [내 정수 0 .. 1000000000 ];
배열 B의 각 요소는 다음 값 중 하나를 가질 수있는 정수입니다. 0, 1;
A의 요소는 모두 다릅니다.
```

## 원문
```text
You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

0 represents a fish flowing upstream,
1 represents a fish flowing downstream.
If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A and B such that:

  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0
Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.

Write a function:

function solution(A, B);

that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.

For example, given the arrays shown above, the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000];
each element of array B is an integer that can have one of the following values: 0, 1;
the elements of A are all distinct.
```