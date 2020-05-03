function solution(A) {
  const set = new Set(A)
  for (let i = 1, len = set.size; i <= len; i++) {
    if (!set.has(i)) return i;
  }
  return set.size + 1;
}

console.log(
  solution([1, 3, 6, 4, 1, 2]) === 5,
  solution([1, 2, 3]) === 4,
  solution([-1, -3]) === 1
);
