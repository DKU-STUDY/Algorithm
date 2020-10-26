function solution (S) {
  const N = S.length;
  if (S.indexOf('aaa') !== -1) return -1;
  const filtered = S.split('').filter(v => v !== 'a');
  if (filtered.length === 0) return 0;
  const result = filtered.reduce((str, c) => str + c + "aa", "aa");
  return result.length - N;
}

console.log(solution('aabab'), 3);
console.log(solution('dog'), 8);
console.log(solution('aa'), 0);
console.log(solution('baaaa'), -1);
