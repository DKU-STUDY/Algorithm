## 문제
https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/

## 입출력
```javascript
function solution(S) {
    // write your code in JavaScript (Node.js 8.9.4)
    return 0;
}
console.log(
  solution('{[()()]}') === 1,
  solution('([)()]') === 0
)
```

## 번역
```text
다음 조건 중 하나라도 해당되는 경우 N 문자로 구성된 문자열 S는 올바르게 중첩 된 것으로 간주됩니다 .

S는 비어 있습니다.
S의 형식은 " (U) "또는 " [U] "또는 " {U} "입니다. 여기서 U는 올바르게 중첩 된 문자열입니다.
S의 형식은 " VW "이며 여기서 V와 W는 올바르게 중첩 된 문자열입니다.
예를 들어, 문자열 " {[() ()]} "은 (는) 올바르게 중첩되었지만 " ([) ()] "는 그렇지 않습니다.

함수를 작성하십시오.

기능 솔루션 (S);

N 문자로 구성된 문자열 S가 주어지면 S가 올바르게 중첩되면 1을, 그렇지 않으면 0을 반환합니다.

예를 들어, S = " {[() ()]} "인 경우 함수는 1을 리턴하고 S = " ([) ()] "인 경우 함수는 위에서 설명한대로 0을 리턴해야합니다.

다음 가정을위한 효율적인 알고리즘을 작성하십시오 .

N은 [ 0 .. 200,000 ] 범위 내의 정수 이며;
문자열 S는 " ( ", " { ", " [ ", " ] ", " } "및 / 또는 " ) " 문자로만 구성됩니다 .
```

## 원문
```text
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

function solution(S);

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
```