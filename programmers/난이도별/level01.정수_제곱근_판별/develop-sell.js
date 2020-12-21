function solution(n) {
  //n을 루트씌운 것이 integer인지에 따라 -1, x+1의 제곱을 리턴
  const num = Math.sqrt(n)
  return Number.isInteger(num) ? (num+1)*(num+1) : -1 ;
}

문제풀이:
n을 루트씌운 것이 integer인지 아닌지에 따라 -1, x+1의 제곱을 리턴한다.

사용 함수: 
Math.sqrt(n) : 제곱근을 구하는 함수
Number.isInteger(num) : 정수인지 아닌지 확인하는 함수 (return true or false)

배운 점:
제곱하는 함수가 생각 안 나서 위에 식처럼 풀었다. 
(num) ** 2  : 제곱하는 함수 ( 숫자 ** 2 / 숫자 ** 3 이면 세제곱)