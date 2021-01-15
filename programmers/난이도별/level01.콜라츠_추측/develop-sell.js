function solution(num) {
  let answer = 0;
  while(1){
      if(answer == 500)
          return -1;
      if(num == 1)
          break;
      num % 2 == 0 ? num /= 2 : num = (num * 3) + 1  
      answer++;
  }
  return answer;
}

// 문제풀이:
// 짝수면 나누기 2, 홀수면 3 곱하고 + 1 해준다. 
// 언제까지? 숫자가 1이 되거나, 돌린 횟수가 500번이 되는 경우(return -1)

// 아쉬운점:
// eyabc.js님 코드 확인 후 무한루프가 아니라, 
// num != 1로 돌리면 한 줄 더 줄일 수 있음을 알게 되었다. 

//변경 된 코드 
  // while(num != 1){
  //     if(answer == 500)
  //         return -1;
  //     num % 2 == 0 ? num /= 2 : num = (num * 3) + 1  
  //     answer++;
  // }

// 프로세스를 이렇게 함수로 명칭해서 보니까 눈으로 보기 좋음을 알게 되었습니다. 
// 앞으론 네이밍도 한번 도전해보겠습니다. 
// const process = (num) => isEven(num) ? num / 2 : num * 3 + 1;