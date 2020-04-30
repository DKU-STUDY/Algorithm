function solution(A) {
  let frontSum = 0;
  let backSum = A.reduce((sum, value) => sum + value);
  const len = A.length - 1;
  return A.reduce((min, v, k) => {
    if (k === len) return sum;
    frontSum += v;
    backSum -= v;
    const diff = Math.abs(frontSum - backSum);
    if (k === 0 || diff < sum) return diff;
    return sum;
  }, 0);
}
console.log(solution([3, 1, 2, 4, 3]) === 1);
console.log(solution([-1000, 1000]) === 2000);
