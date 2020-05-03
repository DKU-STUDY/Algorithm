function solution (A) {
  return [ ...A.reduce((set, v) => (
    set[set.has(v) ? 'delete' : 'add'](v), set
  ), new Set) ][0]
}

console.log(
  solution([9, 3, 9, 3, 9, 7, 9]) === 7
)