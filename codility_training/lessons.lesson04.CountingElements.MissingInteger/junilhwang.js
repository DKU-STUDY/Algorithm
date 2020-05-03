function solution(A) {
  const idx = [ ...new Set(A.sort((a, b) => a - b)) ].findIndex((v, k) => v-1 !== k)
  return idx === -1 ? A.length : idx + 1
}

console.log(
  solution([1, 3, 6, 4, 1, 2]) === 5,
  solution([1, 2, 3]) === 4,
  solution([-1, -3]) === 1
);
