function solution(H) {
  const stack = [H[0]];
  let res = 1;
  for (const v of H) {
    while(stack[stack.length - 1] > v) stack.pop();
    if (v > stack[stack.length - 1] || stack.length === 0) res++;
    stack.push(v)
  }
  return res;
}
console.log(
  solution([8, 8, 5, 7, 9, 8, 7, 4, 8]) === 7
);