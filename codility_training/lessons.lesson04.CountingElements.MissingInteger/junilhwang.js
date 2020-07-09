function solution(A) {
  const set = new Set(A)
  for (let i = 1, len = set.size; i <= len; i++) {
    if (!set.has(i)) return i;
  }
  return set.size + 1;
}

function solution2(A) {
  const obj = {}
  for (const v of A) obj[v] = true
  const len = Object.entries(obj).length
  for (let i = 1; i <= len; i++) {
    if (!obj[i]) return i;
  }
  return len + 1;
}

console.log(
  solution2([1, 3, 6, 4, 1, 2]) === 5,
  solution2([1, 2, 3]) === 4,
  solution2([-1, -3]) === 1
);
