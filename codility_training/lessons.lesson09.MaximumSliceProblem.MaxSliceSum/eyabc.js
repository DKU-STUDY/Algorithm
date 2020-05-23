function solution(A) {
  let max_ending = 0;

  return A.reduce((max, v) => {
    max_ending = Math.max(v, max_ending + v);
    return Math.max(max, max_ending);
  }, -1000000)
}

console.log(
  solution([3, 2, -6, 4, 0])===5,
  solution([-10]) === -10,
  solution([-2, 1]) === 1
);