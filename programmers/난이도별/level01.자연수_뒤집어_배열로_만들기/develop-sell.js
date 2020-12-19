//첫번째 방법 
function solution(n) {
  let answer = [];
  n = n + "";
  let len = n.length
  for(let i = 0; i < len; i++){
      answer.push(n[len - i - 1] * 1);
  }
  return answer;
}

// 문제풀이: 
// 숫자를 문자로 형변환 후, char 한 글자씩 반대로 접근(len - i -1)해서 answer 배열에 추가(push)한다. 

//2번째 방법 
function solution(n) {
  return n.toString().split("").reverse().map((char)=> (Number(char)))
}

// 알게된 점: 
// reverse()라는 함수가 존재하는걸 깜빡했네요!! 
// 배열 크기 그대로 안의 내용을 바꿀 때 (여기선 문자 -> 숫자로 변경) map() 함수를 사용하면 효율적이다. 

// toString == n + "" (숫자 -> 문자)
// Number(char) == n * 1 (문자 -> 숫자)

//eyabc.js 님 코드 확인 후 변경
function solution(n) {
  return n.toString()
          .split("")
          .reverse()
          .map((char)=> (Number(char)))
}