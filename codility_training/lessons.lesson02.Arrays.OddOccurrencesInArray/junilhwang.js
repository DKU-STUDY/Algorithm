function solution (A) {
  return [ ...A.reduce((set, v) => {
    set.has(v) ? set.delete(v) : set.add(v)
    return set
  }, new Set) ][0]
}

console.log(
  solution([9, 3, 9, 3, 9, 7, 9]) === 7
)