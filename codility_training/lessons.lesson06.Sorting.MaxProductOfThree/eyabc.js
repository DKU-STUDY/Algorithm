function solution (A) {
  const aLen = A.length;
  let res = 1;
  let cnt = 0;
  A.sort((a, b) => Math.abs(b) - Math.abs(a));
  console.log(A);
  for (let i = 0 ; i < aLen ; i++) {
    if(cnt === 0) {
      res *= A[i];
      cnt++;
    }
    if(cnt === 1) {

    }


  }

  return res;
}

console.log(
  // solution([-3, 2, 2, -2, 5, 6]) === 60,
  // solution([-5, 5, -5, 4]) === 125,
  solution([-4, -6, 3, 4, 5]) === 120
);
