function solution(s) {
  let answer = '';
  let isOdd = true;
  if (s.length % 2 == 0)
      isOdd = false;
  if (isOdd == true){
      //홀수
      for(let i = 0; i < s.length; i++){
          //아래 콘솔 2개는 소수점으로 자동 형변환하는 걸 확인하기 위함 
          console.log(s.length / 2)
          console.log(i)  
          if(i == s.length / 2 - 0.5){
              return s.charAt(i)
          }
      }
  }
  else{
      //짝수
      for(let i = 0; i < s.length; i++){
          if(i === s.length / 2){
              return s.charAt(i-1) + s.charAt(i);
          }
      }
  }
  
  return answer;
}

// 원리:
// - 홀수, 짝수 분기 처리해서 진행했습니다.
// - isOdd가 true면 홀수, 아니면 짝수입니다
// - 홀수의 경우 가운데 1자만 빼고, 짝수는 2자를 빼게 됩니다. 

// 헷갈린점:
// 1. 
// - 네이밍에서 isOdd로 했는데, 말 그래도 Odd(홀수)인지를 묻는 걸로 네이밍했으면 그렇게 믿어야함
// - 즉, isOdd가 true면 홀수이고, 아니면 짝수인건데 반대로 생각하고 있었다 
// 2. 
// - 홀수에서 s.length와 i가 같을 때 return s.charAt(i) 가운데 한 글자만 빼려고 했는데
// - s.length / 2 가 처음에 몫만 나오는 줄 알았는데, js는 저절로 형변환을 해서 소수점이 나오게 된다
// - ex. 5 -> 2.5가 나옴!! (c언어는 안 그랬던거 같은데... 아닌가? )
// - 자동 형변환 잘 확인할 것 ! 

// 다른 사람 코드 참고 (eyabc.js)
// const middle = s.length / 2;
// const floor = ~~middle;
// return (Number.isInteger(middle) ? s[floor - 1] : '') + s[floor];

// 정확히 반 나눈 middle(소수점 포함 값)이 int가 아니면 홀수니까 s[floor]만
// 짝수면 s[floor - 1] + s[floor] 로 return 한다

//double tilde( ~~ ) 연산자 : Math.floor() 연산자와 비슷하다 => "내림" 같은 표현 (소수점 없애는)
// 양수에선 결과가 같으나 음수에선 결과가 다르다
// var num1 = 1234.5678;
// var num2 = -5.9;

// console.log(Math.floor(num1));
// console.log(~~num1);
// console.log('---');
// console.log(Math.floor(num2));
// console.log(~~num2);

// > 1234
// > 1234
// > ---
// > -6
// > -5

// 참고자료 : https://dreamyoungs.github.io/js/tilde-and-double-tilde-operator

// 느낀점: 
// 애초에 for문 돌릴 필요가 없었고, s.length의 가운데 값의 해당되는 문자를 빼면 되었다.