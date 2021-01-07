function solution(dartResult) {
  let answer = 0;
  let temp = 0;
  let checkoption = true;
  let post = 0;
  
  const pow = (num, upper) => (Math.pow(num, upper))
  
  //삼항연산자로 3개의 조건을 걸 수 있는 방법은 없는가? 
  function pow_num (num, char){
      if(char === 'S') {
          return num;
       }
      if (char === 'D') {
          return pow(num, 2);
       }
      
       return pow(num, 3)
  }
  
  function option_num(num, char){
      if(char === '*'){
          answer = answer - post + post * 2;
          return num * 2;
      }
      else{
          return num * (-1);
      }
  }
  
  dartResult = dartResult.split('')
  let len = dartResult.length
  let char = ''
  for(let i = 0; i < len; i++){
      char = dartResult[i]
      //integer인지, float인지, string인지, array인지 아는 방법 찾기 
      if (char * 1 >= 0 && char * 1 <= 10 ){
          if (checkoption === false){
              answer += temp;
              post = temp
          }
          if (char * 1 === 1){
              if(dartResult[i+1] * 1 === 0 ){
                  i ++;
                  temp = 10
              }
              else
                  temp = char * 1;
          }
          else{
          
          temp = char * 1;
          }
      }
      else if (char === 'S' || char === 'D' || char === 'T'){
          
          temp = pow_num(temp, char);
          checkoption = false;
      }
      else{
          if(checkoption === false){
              checkoption = true
              temp = option_num(temp, char)
              answer += temp;
              post = temp
          }
          
      }
  }
  if(dartResult[len - 1] !== '*' && dartResult[len - 1] !== '#')
      answer += temp
  return answer;
}

// 문제풀이: 
// 먼저 숫자인지, S,D,T인지, opiton인지에 따라 분기처리 했습니다. 
// 숫자의 경우, 만약 숫자가 10이면 i ++해서 다음 index는 실행하지 않게 하고, 대신 temp(현재 변하는 값을 담는 변수)를
// 10으로 설정했습니다. 

// S,D,T의 경우가 가장 쉬웠는데, 
// 문자에 따라 제곱하는 숫자가 다르도록 함수를 짜서 진행했습니다. 

// 마지막 옵션의 경우 
// *이면 전 값도 두배로 하는 부분이 까다로웠습니다. 
// 이걸 다른 분들 코드 보니까, 아예 1회차,2회차마다 값을 저처럼 answer에 더하는게 아니라
// 어떠한 배열에 1회차, 2회차 값 별로 정리하는게 * 옵션을 다룰 때 훨씬 좋겠다는 생각했습니다. 

// #이면 현재 값을 -1을 곱해주면 되어서 쉬었습니다. 

// 마지막으로 옵션은 말그대로 옵션이라서 
// 있을 수도, 없을 수도 있는데 
// 그걸 판단하기 위해 checkoption 변수를 둬서 
// checkoption은 S,D,T 분기 부분 끝나고 무조건 false로 만들게 했고, 

// 그 다음 옵션과 숫자로 가는데, 
// 만약 숫자로 가게 되면 옵션이 없이 연산이 끝난거니까, 바로 temp를 answer에 더했습니다. 
// 그리고 전 값이 필요해서 post 변수에 temp를 저장했습니다. 

// 옵션으로 가게 되어도 이 부분을 추가했습니다. 

// 후기: 
// 와우... 처음으로 긴 알고리즘을 풀었는데 너무 어려웠네요,
// 혹시 더 좋은 코드 있으면 알려주시면 감사하겠습니다!
