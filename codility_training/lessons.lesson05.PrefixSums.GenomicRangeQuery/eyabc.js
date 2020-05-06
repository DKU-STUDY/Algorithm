/* https://github.com/yaseenshaik/codility-solutions-javascript/blob/master/GenomicRangeQuery.md
* 어려워서 구글링을 하였다. */
function solution(S, P, Q) {
  return Q.map((q, k) => {
    const val = S.slice(P[k], q+1);
    if(val.indexOf('A') !== -1) return 1;
    else if (val.indexOf('C') !== -1) return 2;
    else if (val.indexOf('G') !== -1) return 3;
    else if (val.indexOf('T') !== -1) return 4;
  });
}

console.log(
  // solution('TC', [0, 0, 1], [0, 1, 1]),
  solution('TC', [0, 0, 1], [0, 1, 1]).toString() ===[4, 2, 2].toString(),
  solution('CAGCCTA', [2, 5, 0], [4, 5, 6]).toString() === [2, 4, 1].toString(),
  solution('AC', [0, 0, 1], [0, 1, 1]).toString() ===  [1, 1, 2].toString()
);

/* time out */
function solution2(S, P, Q) {
  const len = P.length;
  const arr = [];
  const sString = S.split('').map(v => {
    switch (v) {
      case 'A' : return 1;
      case 'C' : return 2;
      case 'G' : return 3;
      case 'T' : return 4;
    }
  });
  for(let i = 0; i < len; i++) {
    arr.push(Math.min(...sString.slice(P[i], Q[i]+1)));
  }
  return arr
}