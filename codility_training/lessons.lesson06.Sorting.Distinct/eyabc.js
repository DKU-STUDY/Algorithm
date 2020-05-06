function solution(A) {
  return new Set(A).size;
}
console.log(solution([2, 1, 1, 2, 3, 1]) === 3);