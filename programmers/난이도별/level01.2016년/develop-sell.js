function solution(a, b) {
  var answer = '';
  const day_week = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
  const month_day = [31,29,31,30,31,30,31,31,30,31,30,31];
  let total_day = 0;
  for(let i= 0; i < a-1; i++){  //for(let i= 1; i < a; i++) 로 작성했었음
      total_day += month_day[i];
  }
  total_day += b;
  answer = day_week[(total_day + 4) % 7];
  
  return answer;
}

//생각보단 쉬운 문제였는데 못 풀었다.
// khw970421님의 풀이를 보고 알 수 있었다
// for문에서 1과 a / 0과 a-1 이 무엇이 다른건지 고민하다가 
// month_day[i]를 가져오는 부분에서 -1를 안해줬다는걸 알게 되었다..!! 
// 다음부턴 웬만하면 for문의 앞은 0으로 고정해서 하는걸로.. 자칫 잘못하면 헷갈리겠다 (시간낭비)