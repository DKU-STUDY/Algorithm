const createPeaks = (A) => {
  const len = A.length;
  const peaks = new Array(len).fill(false);
  for (let i = 1; i < len - 1; i++) {
    if (A[i] > Math.max(A[i - 1], A[i + 1])) {
      peaks[i] = true;
    }
  }
  return peaks;
};

/* Check whether x flags can be set
*  If we know that x flags can be set,
* then we also know that x−1, x−2, . . . , 1 flags can be set.
* Otherwise, if x flags cannot be set, then x+1, x+2, . . . , √ N flags cannot be set either.
* */
const check = (x, A) => {
  const N = A.length;
  const peaks = createPeaks(A);
  let flags = x;
  let pos = 0;
  while (pos < N && flags > 0) {
    if (peaks[pos]) {
      flags -= 1;
      pos += x;
    }
    else
      pos += 1;
  }
  return flags === 0;
};

/* Next peak
*
* */
const next_peak = A => {
  const N = A.length;
  const peaks = createPeaks(A);
  console.log({peaks});
  const next = new Array(N).fill(0);
  next[N - 1] = -1;
  for (let i = N - 2; i > -1; i--) {
    if (peaks[i])
      next[i] = i;
    else
      next[i] = next[i + 1]
  }
  return next
};


function solution(A) {
  const N = A.length;
  const next = next_peak(A);
  let i = 1, jumps = 0;
  while((i - 1) * i <= N) {
    let pos = 0, num = 0;
    while (pos < N && num < i) {
      pos = next[pos];
      if (pos == -1)
        break;
      num += 1;
      pos += i;
    }
    jumps = Math.max(jumps, num);
    i += 1
  }
  return jumps
}

console.log(
  solution([1, 3, 1, 4, 1]) === 2,
  solution([0, 1000000000, 0]) === 1,
  solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) === 3,
  solution( [0, 0, 0, 0, 0, 1, 0, 1, 0, 1]) === 2,
);