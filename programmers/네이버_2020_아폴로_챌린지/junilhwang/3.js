function solution(play_list, listen_time) {
  const arr = [];
  for (const [k, v] of Object.entries(play_list)) {
    arr.push(...Array(v).fill(Number(k)));
  }
  const arr2 = [ ...arr.slice(-listen_time), ...arr.slice(0, listen_time) ];
  let max = 0;
  for (let i = 0, len = arr.length; i < len; i++) {
    max = Math.max(max, new Set(arr.slice(i, i + listen_time)).size);
  }
  for (let i = 0, len = arr2.length; i < len; i++) {
    max = Math.max(max, new Set(arr2.slice(i, i + listen_time)).size);
  }
  return max;
}

console.log(
  solution([2, 3, 1, 4],3) == 3,
  solution([1, 2, 3, 4],5) == 4,
  solution([1, 2, 3, 4],20) === 4,
)