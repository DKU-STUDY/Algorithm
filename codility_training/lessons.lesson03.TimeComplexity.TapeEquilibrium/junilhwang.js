function solution(A) {
  return A.slice(0, -1).reduce(([min, front, back], a) =>
    [ Math.min(Math.abs(front - back + a * 2), min), front + a, back - a ],
    [ Infinity, 0, A.reduce((a, b) => a + b) ])[0]
}

console.log(
  solution([3, 1, 2, 4, 3]) === 1,
  solution([-1000, 1000]) === 2000,
  solution([1, 2]) === 1
);