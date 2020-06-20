# 출처

https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/

# 번역
```text
일부 사각형의 영역을 나타내는 정수 N이 제공됩니다.

변의 길이가 A이고 B 인 직사각형 의 넓이 는 A * B이고 둘레 는 2 * (A + B)입니다.

목표는 면적이 N 인 직사각형의 최소 둘레를 찾는 것입니다.이 직사각형의 변은 정수만되어야합니다.

예를 들어, 정수 N = 30 인 경우 영역 30의 사각형은 다음과 같습니다.

(1, 30), 둘레 62의
(2, 15), 둘레가 34,
둘레가 26 인 (3, 10)
(5, 6), 둘레는 22입니다.
함수를 작성하십시오.

기능 솔루션 (N);

정수 N이 주어지면 면적이 정확히 N 인 사각형의 최소 둘레를 반환합니다.

예를 들어, 정수 N = 30 인 경우 함수는 위에서 설명한대로 22를 반환해야합니다.

다음 가정을위한 효율적인 알고리즘을 작성하십시오 .

N은 [ 1 .. 1,000,000,000 ] 범위 내의 정수 이다.
```

# 원문
```
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

class Solution { public int solution(int N); }

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
```
