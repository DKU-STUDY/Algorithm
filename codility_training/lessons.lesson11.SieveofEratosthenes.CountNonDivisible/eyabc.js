function solution(A) {
  return A.map(v => A.filter(w => v < w || v % w).length);
}
console.log(
  solution([3, 1, 2, 3, 6])
)