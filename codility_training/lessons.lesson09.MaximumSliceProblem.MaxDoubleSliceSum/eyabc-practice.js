/* 9.1 Maximum slice O(n^3)*/
function solution (A) {
  const len = A.length;
  let result = 0;

  for (let p = 0; p < len ; p++) {
    for(let q = p; q < len ; q++) {
      let sum = 0;
      for (let i = p; i < q + 1; i++) {
        console.log({ p, q, i })
        sum += A[i];
      }
      result = Math.max(result, sum)
    }
  }
  return result;
}

/* 9.2 */
function solution2 (A) {
  const len = A.length;
  let result = 0;

  for(let p = 0; p < len ; p++) {
    let sum = 0;
    for(let q = p; q < len; q++) {
      sum += A[q];
      result = Math.max(result, sum)
    }
  }
  return result;
}

/* 9.3 */
function solution3 (A) {
  let max_ending = 0, max_slice = 0;

  for (let a = 0 ; a < A.length; a++) {
    console.log({max_ending, max_slice});
    max_ending = Math.max(0, max_ending + A[a]);
    max_slice = Math.max(max_slice, max_ending);
  }
  return max_slice;
}
console.log(solution3([5, -7, 3, 5, -2, 4, -1]))

console.log(solution3([3, 2, 6, -1, 4, 5, -1, 2]))
