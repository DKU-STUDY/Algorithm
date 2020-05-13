/* JeongShin 님꺼 참고해서 수정 */
function solution(S) {
  const brackets = {
    '(': ')',
    '{': '}',
    '[': ']'
  };
  const sLen = S.length;
  const stack = [];
  const start = /\[|\(|{/;

  for (let i = 0 ; i < sLen ; i++) {
    if(start.test(S[i])) stack.push(S[i]);
    else if (S[i] !== brackets[stack.pop()]) return 0;
  }
  return stack.length === 0 ? 1 : 0;
}

console.log(
  solution('{[()()]}') === 1,
  solution('([)()]') === 0
);