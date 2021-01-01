function solution(s, n) {
  let arr = s.split("");
  let ans_arr = []
  let num = 0;
  arr.forEach(e => {
      if(e === " "){
          ans_arr.push(e);
          return;
      }
      num = e.charCodeAt(0)
      if(num >= 65 && num <= 90){
          if(num + n > 90){
              ans_arr.push(String.fromCharCode(num+n - 26))
          }
          else
              ans_arr.push(String.fromCharCode(num+n))
      }
      else{
          if(num+n > 122){
              ans_arr.push(String.fromCharCode(num+n - 26))
          }
          else
              ans_arr.push(String.fromCharCode(num+n))
      }  
  })
  return ans_arr.join("");
}

// 문제풀이:
// 먼저 split함수로 str을 배열로 만들고, 
// 배열을 forEach문으로 돌면서 n값만큼 더해준 값을 다시 ans_arr에 push하고,
// ans_arr를 join함수로 다시 str로 바꿔서 제출한다. 

// 사용한 함수:
// char.charCodeAt(0): 영문자인 char를 숫자로 바꿔주는 함수
// String.fromCharCode(num): 숫자인 num을 영문자로 바꿔주는 함수 

// 알게된 점:
// 1. str함수인 split를 통해 str를 배열로 만들기 
// 2. forEach문은 continue문이 안 먹힌다.. return문 사용해야 함
// 3. array함수인 join을 통해 배열의 모든 요소의 병합을 str로 바꿔준다 
