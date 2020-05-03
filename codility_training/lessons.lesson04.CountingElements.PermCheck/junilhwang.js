function solution(A) {
  return !(A.sort((a, b) => a - b).find((v, k) => v - 1 === k)) * 1
}

console.log(
  solution( [4, 1, 3, 2]) === 1,
  solution([4, 1, 3]) === 0,
)