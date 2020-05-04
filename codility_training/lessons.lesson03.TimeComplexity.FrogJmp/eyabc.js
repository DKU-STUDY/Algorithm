function solution(X, Y, D) {
  return Math.ceil((Y - X) / D);
}

console.log(solution(10, 85, 30));

function solution2(X, Y, D) {
  let count = 0;
  while(X < Y) {
    X += D;
    count++;
  }
  return count;
}
