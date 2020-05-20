/* Correctness 100% Performance 14% (2 wrong answers) */
function solution(A) {
  let res = 0;
  for (let m = 1; m < A.length - 1; m++) {
    let lower_max_ending = 0, lower_max_slice = 0, upper_max_ending = 0, upper_max_slice = 0;
    console.log('---------------------')
    for(let i = 1; i < m; i++) {
      lower_max_ending = Math.max(0, lower_max_ending + A[i]);
      lower_max_slice = Math.max(lower_max_slice, lower_max_ending);
      console.log({i, lower_max_ending, lower_max_slice});
    }
    for(let i = m + 1; i < A.length - 1 ; i++) {
        // console.log({i, upper_max_ending, upper_max_slice});
      upper_max_ending = Math.max(0, upper_max_ending + A[i]);
      upper_max_slice = Math.max(upper_max_slice, upper_max_ending);
    }
    console.log({m, lower_max_slice, upper_max_slice})
    res = Math.max(res, lower_max_slice + upper_max_slice)
  }

  return res;
}

console.log(solution([5, -7, 3, 5, -2, 4, -1]))
// console.log(solution([3, 2, 6, -1, 4, 5, -1, 2]))
  // === 17

