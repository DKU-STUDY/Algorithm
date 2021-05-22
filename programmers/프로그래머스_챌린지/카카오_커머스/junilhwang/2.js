/* 실패
function solution(m, values) {
  const arr = [];
  for (const value of values) {
    const index = arr.findIndex(sum => sum + value <= m)
    if (index === -1) {
      arr.push(value);
    } else {
      arr[index] += value;
    }
  }
  return arr.length;
}
*/

function solution(m, values) {
  const arr = [];
  for (const value of values) {
    let index = -1;
    if (arr.length === 0) {
      arr.push(value);
      continue;
    }
    for (let i = arr.length - 1; i >= 0; i--) {
      if (arr[i] + value > m) break;
      index = i;
    }
    if (index === -1) {
      arr.push(value);
      continue;
    }
    arr[index] += value;
  }
  return arr.length;
}

console.log(
  // [solution(4, [2,3,1]), 2],
  // [solution(4, [3,2,3,1]), 3],
  // [solution(4, [3,2,3,1,2]), 4],
)