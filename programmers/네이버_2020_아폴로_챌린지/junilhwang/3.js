function solution(play_list, listen_time) {
  let max = 0;
  for (let i = 0, len = play_list.length; i < len; i++) {
    let cnt = 1;
    let n = listen_time - 1;
    for (let j = i + 1; j < len && n > 0; j++) {
      const v = play_list[j];
      if (n >= 1) {
        n -= v;
        cnt += 1;
      }
    }
    for (let j = 0; j < len && n > 0 && cnt < len; j++) {
      const v = play_list[j];
      if (n >= 1) {
        n -= v;
        cnt += 1;
      }
    }
    max = Math.max(cnt, max);
  }
  return Math.min(max, play_list.length);
}

console.log(
  solution([2, 3, 1, 4],3) == 3,
  solution([1, 2, 3, 4],5) == 4,
  solution([1, 2, 3, 4],20) === 4,
)