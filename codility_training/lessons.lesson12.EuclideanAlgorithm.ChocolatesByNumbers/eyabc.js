function solution (N, M) {
  const arr = new Array(N).fill(true);
  let i = 0;
  let cnt = 0;
  while(arr[i]) {
    arr[i] = false;
    cnt++;
    i = (i + M) % N;
  }
  return cnt;
}

console.log(
  solution(10, 4)
  // === 5,
);

/*
  i = (i + M) % N ; 이라면
  I(0)  M(4)  N(10)  res()

*/
