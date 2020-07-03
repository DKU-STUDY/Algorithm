function solution (A) {
  const len = A.length;
  const cnt = A.reduce((cnt, v) => {
    cnt[v] = cnt[v] ? cnt[v] + 1 : 1;
    return cnt;
  }, {});

  return A.map(v => {
    let divisor = 0;
    for (let j = 1 ; j * j <= v ; j++) {
      if (v % j === 0) {
        divisor += cnt[j] || 0;
        if (v / j !== j)
          divisor += cnt[v / j] || 0;
      }
    }
    return len - divisor;
  });
}

console.log(
  solution([3, 1, 2, 3, 6]),
  solution([2]),
  solution([ 6, 7, 2, 1, 4, 7, 4, 4, 1, 8, 10, 15 ])
);

