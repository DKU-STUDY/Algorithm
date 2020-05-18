function solution(H) {
  const stack = [H[0]];
  stack.getLast = () => stack[stack.length - 1]
  let res = 1;
  for (const v of H) {
    while(stack.getLast() > v) stack.pop();
    res += v > stack.getLast() || !stack.length;
    stack.push(v)
  }
  return res;
}
console.log(
  solution([8, 8, 5, 7, 9, 8, 7, 4, 8]) === 7
);
