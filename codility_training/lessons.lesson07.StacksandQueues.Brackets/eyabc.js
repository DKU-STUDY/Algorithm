/* JeongShin 님꺼 참고해서 수정 */
function solution(S) {
  const brackets = {
    '(': ')',
    '{': '}',
    '[': ']'
  };
  const stack = [];
  const start = /\[|\(|{/;

  for (const v of S) {
    if(start.test(v)) stack.push(v);
    else if (v !== brackets[stack.pop()]) return 0;
  }
  return !stack.length * 1;
}

console.log(
  solution('{[()()]}') === 1,
  solution('([)()]') === 0,
  solution('{{{{') === 0
);