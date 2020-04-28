function solution(A) {
  const set = new Set(A);
  const len = set.size;
  let i = 1;
  for(; i < len + 1; i++) {
    if(!set.has(i)) return i;
  }
  return i;
}
console.log(
  solution([1, 3, 6, 4, 1, 2])===5,
  solution([1, 2, 3])===4,
  solution([-1, -3])===1
);
