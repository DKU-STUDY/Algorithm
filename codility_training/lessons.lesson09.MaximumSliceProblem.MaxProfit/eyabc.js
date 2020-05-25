function solution(A) {
  if(!A.length) return 0;
  const arr = [...A].reverse();
  let max, maxmap;
  const len = A.length;

  const maxArr = arr.map(v => {
    maxmap = maxmap ? (maxmap < v ? v : maxmap) : v;
    return maxmap
  });
  maxArr.reverse();

  for(let i = 0 ; i < len - 1 ; i++)
    max = A[i] < maxArr[i] ? Math.max(maxArr[i] - A[i], (max || maxArr[i] - A[i])) : max;

  return max || 0;
}

/* time out */
function solution2(A) {
  if(!A.length) return 0;
  let max;
  const len = A.length;

  for(let i = 0 ; i < len ; i++) {
    const buy = A[i];
    for (let j = i ; j < len ; j++) {
      const sell = A[j];
      max = Math.max(sell - buy, (max || sell - buy));
    }
  }
  return max;
}
function solution3(A) {
  if(!A.length) return 0;
  let max;
  const len = A.length, maxArr= [];

  for(let i = 0 ; i < len - 1 ; i++) {
    maxArr[i] = Math.max(...A.slice(i+1, len))
  }
  for(let i = 0; i < maxArr.length; i++) {
    max = A[i] < maxArr[i] ? Math.max(maxArr[i] - A[i], (max || maxArr[i] - A[i])) : max
  }
  return max || 0;
}
function solution4(A) {
  if(!A.length) return 0;
  const arr = [...A];
  let max;
  const len = A.length, maxArr = [];

  for(let i = 0 ; i < len - 1 ; i++) {
    arr.shift()
    maxArr[i] = Math.max(...arr)
    max = A[i] < maxArr[i] ? Math.max(maxArr[i] - A[i], (max || maxArr[i] - A[i])) : max
  }
  return max || 0;
}
console.log(
  solution([23171, 21011, 21123, 21366, 21013, 21367]),
  solution([5, 4, 3, 2, 1] ),
  solution([])
  // =;== 356
)