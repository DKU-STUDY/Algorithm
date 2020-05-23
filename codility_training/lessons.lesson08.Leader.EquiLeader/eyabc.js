function solution (A) {
  let res = 0;
  const len = A.length - 1;
  const lObj = {}, rObj = {};

  const setSize = (new Set(A)).size;
  if (setSize > (A.length / 2)) return 0;

  for (const v of A)
    rObj[v] = (rObj[v] || 0) + 1;

  for (let i = 0 ; i < len ; i++) {
    lObj[A[i]] = (lObj[A[i]] || 0) + 1;
    rObj[A[i]]--;
    const lMax = Math.max(...Object.values(lObj));
    const rMax = Math.max(...Object.values(rObj));
    /// l r 둘다 과반수가 존재하는지
    if (lMax / (i + 1) > 0.5 && rMax / (len - i) > 0.5) {
      const maxLKey = Object.entries(lObj).find(([, value]) => value === lMax);
      const maxRKey = Object.entries(rObj).find(([, value]) => value === rMax);
      if (maxRKey[0] === maxLKey[0]) res++;
    }
  }
  return res;
}

console.log(
  solution([4, 3, 4, 4, 4, 2]),
  solution([4, 4, 2, 5, 3, 4, 4, 4]),
  solution([-1000000000, -1000000000]),
  solution([1, 2, 3, 4, 5, 6, 7, 8, 9]),
);