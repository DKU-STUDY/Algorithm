function solution(S) {
  const stack = [];
  for (const v of S) {
    if (v === '(') stack.push(v);
    else {
      if(stack.length === 0) return 0;
      stack.pop()
    }
  }
  return !stack.length * 1
}
console.log(
  solution('(()(())())') === 1,
  solution('())') === 0,
  solution('((())') === 0,
  solution('((()))))') === 0,
);