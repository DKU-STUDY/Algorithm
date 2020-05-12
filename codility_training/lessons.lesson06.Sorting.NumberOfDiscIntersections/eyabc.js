const sortAsc = (a, b) => a - b;
/* https://jobjava00.github.io/algorithm/codility/lesson6/NumberOfDiscIntersections/ */
function solution(A) {
  let counter = 0;
  const lower = [];
  const upper = [];
  const aLen = A.length;

  for(let i = 0; i < aLen ; i++) {
    lower[i] = i - A[i];
    upper[i] = i + A[i];
  }
  lower.sort(sortAsc);
  upper.sort(sortAsc);

  for(let i = 0, j = 0 ; i < aLen ; i++) {
    while(j < aLen && upper[i] >= lower[j]){
      counter += j - i;
      j++;
    }
    if(counter > 10000000) return -1;
  }

  return counter;
}

/* timeout */
function solution2 (A) {
  const len = A.length;
  let res = 0;

  A.forEach((centerV, k) => {
    const lowV = k - centerV, highV = k + centerV;
    for(let i = k + 1; i < len ; i++) {
      const _this = A[i], lowThis = i - _this;
      if (lowV >= lowThis || highV >= lowThis) res++;
      if (res > 10000000) return -1;
    }
  });
  return res;
}

/*
0 -> 1, 2, 4
1 -> 0, 2, 3 ,4 , 5
2 -> 0, 1, 3, 4,
3 -> 4, 2, 1
4 -> 1, 0, 2, 3, 5
5 -> 1, 4
 */
console.log(solution([1, 5, 2, 1, 4, 0]) === 11);