function solution(A) {
  return A.reduce(([ max, max_ending ], v) => {
    max_ending = Math.max(v, max_ending + v);
    return [ Math.max(max, max_ending), max_ending ];
  }, [-Infinity, -Infinity])[0]
}

console.log(
  solution([3, 2, -6, 4, 0])===5,
  solution([-10]) === -10,
  solution([-2, 1]) === 1
);
