function solution (k, score) {
  const subMap = {};
  const subMapCnt = {};
  let iterated = 0;
  for (let i = 1, len = score.length; i < len; i++) {
    const key = score[i - 1] - score[i];
    subMap[key] = subMap[key] || new Set();
    subMap[key].add(i);
    subMap[key].add(i - 1);
    subMapCnt[key] = (subMapCnt[key] || 0) + 1;
  }

  return score.length - Object.entries(subMapCnt).reduce((set, [key, cnt]) => {
    if (cnt >= k) {
      return new Set([ ...set, ...subMap[key] ])
    }
    return set;
  }, new Set()).size;
}


console.log(
  solution(3, [24,22,20,10,5,3,2,1]),
  3
)
console.log(
  solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]),
  4
)