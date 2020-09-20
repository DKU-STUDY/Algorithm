function solution(table) {
  const max = table[0].length;
  const tableOf = table.map(v => [ ...v ].reduce((arr, acc, key) => {
    if (acc === 'O') arr.push(key);
    return arr;
  }, []));
  let min = Infinity;
  const f = (set, stack) => {
    if (stack.length > min) return;
    if (set.size === max) {
      min = Math.min(min, stack.length);
      return;
    }
    tableOf.forEach((v, k) => {
      if (stack.includes(k)) return;
      f(new Set([ ...set, ...v]), [ ...stack, k ]);
    })
  }
  f(new Set, []);
  return min;
}

console.log(
  solution(["XOXO", "OXXO", "XXOX", "XOOO"]), 2,
  solution(["OXXO", "XOXO", "XXOO"]), 3,
  solution(["OXOXO", "OOOOO", "XOXOX"]), 1,
)