function solution(s) {
  var answer = false;
  if (s.length === 4 || s.length === 6){
      for(let i = 0; i < s.length; i++){
          if (s.charAt(i) == '0'){
              continue;
          }
          if (isNaN((s.charAt(i)) * 1)){
              return false;
          }
      }
      return true;    
  }
  return false  //맨 마지막에 이 부분을 안 넣어줘서 틀렸다.. 
}

// 코드를 보다보니 조건이 있는것들은 미리미리 없애주는게 좋아보인다
// 이 경우 4, 6이 아니면 바로 return false를 해주는 것이다. 

//아래는 새롭게 짠 코드 
function solution(s) {
  let answer = false;
  //먼저 길이가 4, 6인지 체크한다 (아니면 return false)
  if (s.length !== 4 && s.length !== 6)
      return false;
  
  // for each문으로 바로 char값을 확인한다 (chatAt 쓸 필요 없도록)  
  for (const char of s) {
    if (isNaN(char * 1))
        return false;
  }
  return true;
}