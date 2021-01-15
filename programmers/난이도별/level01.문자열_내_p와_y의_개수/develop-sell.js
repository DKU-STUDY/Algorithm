function solution(s){
  var answer = true;
  var ans = 0;
  for(let i =0; i < s.length; i++){
      let char = s.charCodeAt(i);
      (char === 80 || char === 112) ? ans += 1 : '';
      (char === 89 || char === 121) ? ans -= 1 : '';
  }
  if (ans !== 0){
      answer = false 
  }

  return answer;
}


// 아이디어: 개수만큼 각각 더하고, 빼서 0이면 true, 아니면 false로 되게 만들었다.
// 생각보다 긴 코드로 짠 것 같다.. 

// programmers 한줄코드 
// return s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length;
// toUpperCase : 다 대문자로 만들어버림..!! 
// split : 문자열을 일정한 구분자로 잘라서 배열로 저장하기 위해서 쓴다
// 여기선 각각 P, Y로 split하는데, 갯수가 같으면 같은 값이 나오기에 true가 나온다. 


// 근데 배열로 split이 되는데, 왜 true가 나올까? 배열의 size로 비교하기 때문인가?
// ex. pypy => ["", "y", "y"]  / ypyp => ["", "p", "p"] 
// 라고 생각했는데 뒤에 length가 있었다... ㅎㅎ length가 같은걸로 비교 !! 