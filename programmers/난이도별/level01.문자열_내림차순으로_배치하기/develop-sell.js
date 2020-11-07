function solution(s) {
  var answer = '';
  var ans = [];
  for(let i=0; i < s.length; i++ ){
      ans.push(s.charAt(i))
  }
  ans.sort((a,b) => { return(a-b);})
  
  for(let j =0; j<ans.length; j++){
      answer+= ans(j);
  }
  
  return answer;
}