function solution (A) {
  return A.sort().reduce((sum, v, k) => sum + Math.abs(v - (k + 1)), 0);
}

console.log(solution([1, 2, 1]), 2);
console.log(solution([2, 1, 4, 4]), 1);
console.log(solution([6, 2, 3, 5, 6, 3]), 4);