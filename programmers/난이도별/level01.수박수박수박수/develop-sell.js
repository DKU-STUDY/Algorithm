function solution(n) {
  var answer = '';
  for(var i = 0 ; i<n; i++){
      answer += (i % 2 == 0 ?  '수' : '박')
  }
  return answer;
}

// 처음에는 저번처럼 길게 if문으로 짰다가
// 삼항연산자를 활용해 최대한 코드를 줄여봤다
// Jaewon님의 코드가 효율적인 것 같다 return "수박" * int(n // 2) + "수" * int(n % 2)
// 여기서 '//' 연산자는 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함

// 출처: https://includestdio.tistory.com/16 [includestdio]
