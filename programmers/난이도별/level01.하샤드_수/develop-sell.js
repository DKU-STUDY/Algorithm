function solution(x) {
  let num = (x + '')
                  .split('')
                  .reduce((ans, cur) => (ans * 1 + cur * 1));
  if (x % num !== 0)
      return false;
  return true;
}


// 문제풀이:
// 먼저 숫자를 str로 변환 후, 
// split으로 한 글자씩 arr에 저장한다. 
// 그 후 reduce함수를 통해 각 한 글자씩 더한 값을 구한다. (== num)
// 만약 주어진 x가 num으로 나눠지지 않으면 false, 나눠지면 true이다. 

// 한 줄 코드:
// return !(n % (n + "").split("").reduce((a, b) => +b + +a ));

// js에서 0이면 false, 아니면 true로 인식하니까, 
// 앞에 !(부정)으로 반환해주면 아래 if문을 한 줄 더 줄일 수 있다. 