## 출처
https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/

## 원문
```
Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:

class Solution { public int solution(int N, int M); }

that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..1,000,000,000].
```

## 해석
입력
```javascript
function solution(N, M) {
    // write your code in JavaScript (Node.js 8.9.4)
    return 0;
}
```
- 입력: 양수 N, M
- N : 0 ~ (N-1) 번호가 매겨진 원에 배치된 초콜릿의 수
- 원이기 때문에 로테이션 가능하다.

- 초콜릿을 번호0부터 먹기 시작합니다.
- 다음 먹는 초콜릿의 번호는 (현재번호 + M ) 입니다 

- 다음 먹을 번호에 초콜릿이 없을 때 중단합니다.

- 예시:  N = 10 및 M = 4. 0, 4, 8, 2, 6

- 반환: 먹은 초콜릿의 수


