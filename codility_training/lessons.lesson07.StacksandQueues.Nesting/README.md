## 문제
https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/


## 입출력
```javascript
function solution(S) {
    // write your code in JavaScript (Node.js 8.9.4)
    return 0;
}
console.log(
  solution('(()(())())') === 1,
  solution('())') === 0
)
```
## 번역
```text
다음과 같은 경우 N 문자로 구성된 문자열 S를 올바르게 중첩 이라고 합니다.

S는 비어 있습니다.
S의 형식은 " (U) "입니다. 여기서 U는 올바르게 중첩 된 문자열입니다.
S의 형식은 " VW "이며 여기서 V와 W는 올바르게 중첩 된 문자열입니다.
예를 들어, 문자열 " (() (()) ()) "은 올바르게 중첩되지만 문자열 " ()) "는 그렇지 않습니다.

함수를 작성하십시오.

클래스 솔루션 {public int solution (String S); }

N 문자로 구성된 문자열 S가 주어지면 문자열 S가 올바르게 중첩되면 1을 반환하고 그렇지 않으면 0을 반환합니다.

예를 들어, S = " (() (()) ()) "인 경우 함수는 1을 반환하고 S = " ()) "인 경우 함수는 위에서 설명한대로 0을 반환해야합니다.

다음 가정을위한 효율적인 알고리즘을 작성하십시오 .

N은 [ 0 .. 1,000,000 ] 범위 내의 정수 이며;
문자열 S는 문자 " ( "및 / 또는 " ) " 로만 구성됩니다 .
```
## 원문
```text
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".
```