## 출처
https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/

## 입출력
```javascript
function solution(H) {
    // write your code in JavaScript (Node.js 8.9.4)
    return 0;
}

console.log(
  solution([8, 8, 5, 7, 9, 8, 7, 4, 8]) === 7
);
```

![stoneWall](./StoneWall.png)
## 번역
```text
돌담을 지을 것입니다. 벽은 똑 바르고 N 미터 길이 여야하며 두께는 일정해야합니다. 그러나 장소마다 높이가 달라야합니다. 벽의 높이는 N 양의 정수로 구성된 배열 H로 지정됩니다. H [I]는 I에서 I + 1 미터 (왼쪽 끝)까지의 벽 높이입니다. 특히 H [0]은 벽의 왼쪽 끝의 높이이고 H [N-1]은 벽의 오른쪽 끝의 높이입니다.

벽은 직육면체 석재 블록으로 만들어야합니다 (즉, 그러한 블록의 모든면은 직사각형입니다). 당신의 임무는 벽을 구축하는 데 필요한 최소 블록 수를 계산하는 것입니다.

함수를 작성하십시오.

클래스 솔루션 {public int solution (int [] H); }

즉, 벽의 높이를 지정하는 N 개의 양의 정수로 구성된 배열 H가 있으면 벽을 만드는 데 필요한 최소 블록 수를 반환합니다.

예를 들어 N = 9 개의 정수를 포함하는 배열 H는 다음과 같습니다.

  H [0] = 8 H [1] = 8 H [2] = 5
  H [3] = 7 H [4] = 9 H [5] = 8
  H [6] = 7 H [7] = 4 H [8] = 8
이 함수는 7을 반환해야합니다. 그림은 7 개의 블록으로 구성된 가능한 배열을 보여줍니다.



다음 가정을위한 효율적인 알고리즘을 작성하십시오 .

N은 [ 1 .. 100,000 ] 범위의 정수 이며;
H 어레이의 각 요소는 범위 [내 정수 1 .. 1000000000 ].
```

## 원문 
```text
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

class Solution { public int solution(int[] H); }

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8
the function should return 7. The figure shows one possible arrangement of seven blocks.



Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array H is an integer within the range [1..1,000,000,000].
```