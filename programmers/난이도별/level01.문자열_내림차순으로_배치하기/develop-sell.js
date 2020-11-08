function solution(s) {
  var answer = '';
  var ans = [];
  for(let i=0; i < s.length; i++ ){
      ans.push(s.charAt(i));
  }
  ans.sort((a, b) => a < b ? 1 : -1)
  
  answer = ans.join('');
  
  return answer;
}

// sort하는 부분에서 헤매다가 junilhwang님 코드를 보고 풀었습니다
// join하고도 seperater부분에 ''을 넣어줘야 ','가 안 들어갑니다 (,가 default인가..??)

