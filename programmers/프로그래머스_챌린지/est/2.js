function solution (scores, k) {
  const arr = [];
  const len = scores.length;
  if (scores.length === 1) {
    return 0;
  }

  for (let i = 1; i < len; i++) {
    arr.push({
      k: i,
      v: scores[i] - scores[i - 1],
    })
  }

  const slicePoint = arr.sort((a, b) => b.v - a.v)
                        .slice(0, k - 1)
                        .sort((a, b) => Number(a.k) - Number(b.k));
  let before = 0;
  let sum = 0;
  for (const v of slicePoint) {
    sum += scores[v.k - 1] - scores[before];
    before = v.k;
  }
  return sum + scores[len - 1] - scores[before]
}

console.log(
  solution([1,3,7,8,10,15],3) === 5,
  solution([1,2,12,14,15],2) === 4,
)