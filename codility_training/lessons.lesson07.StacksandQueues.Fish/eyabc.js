function solution (A, B) {
  const down = [];
  const len = A.length;
  let lastSize;
  let aliveCount = 0;

  for (let i = 0; i < len; i++) {
    if (B[i] === 1) down.push(A[i]);
    else {
      while (down.length > 0) {
        lastSize = down[down.length - 1];
        if (lastSize > A[i]) break;
        else down.pop();
      }
      if (down.length === 0) aliveCount++;
    }
  }
  return aliveCount + down.length;
}

console.log(
  solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]),
  // === 2
  // solution([4, 3, 2, 1, 5], [0, 1, 1, 0, 0])
  solution([4], [0])
  // === 2,
);