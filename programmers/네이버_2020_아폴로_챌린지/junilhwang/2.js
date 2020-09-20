
function solution(h, w, n, board) {

  let cnt = 0;
  for (const row of board) {
    let before = 0;
    let next = row.indexOf('0');
    while (next !== -1) {
      if (next - before === 4) cnt += 1;
      [before, next] = [next, row.indexOf('0', next + 1)];
    }
  }

  var answer = -1;
  return answer;
}

console.log(
  solution(7, 9, 4, ["111100000","000010011","111100011","111110011","111100011","111100010","111100000"]), 10,
  // solution(5, 5, 5, ["11111","11111","11111","11111","11111"]), 12,
)