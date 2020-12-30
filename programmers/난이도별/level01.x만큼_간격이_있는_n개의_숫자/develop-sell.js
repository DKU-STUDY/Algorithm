function solution(x, n) {
  let answer = [];
  for(let i = 0; i< n; i++){
      answer.push(x + x * i);
  }
  return answer;
}

// 문제풀이: 
// 간단한 배열 문제였다. 

// 한줄 풀이: 
// return Array(n)
//               .fill(x)
//               .map((v, i) => (i + 1) * v)

// Array(n) : n 크기의 배열을 만든다
// fill(x) : x값으로 배열을 다 채운다 
//  => 만약 이미 다른 값이 들어있어도 x값으로 배열을 다 채워버린다. 
// map((v, i)) : 여기서 v는 값, i는 인덱스이고, "인덱스 + 1" 만큼 값으로 곱해주면 된다. 

