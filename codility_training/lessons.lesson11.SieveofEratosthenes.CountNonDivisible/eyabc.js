function solution (A) {
  const sortedA = [...A];
  const len = A.length;
  sortedA.sort((a, b) => a - b);

  return A.map(v => {
      let index = sortedA.lastIndexOf(v);
      let res = 0;
      for (let i = 0 ; i < index ; i++)
        if (v % sortedA[i] === 0) res++;
      return len - res - 1;
    },
  );
}

console.log(
  solution([3, 1, 2, 3, 6]),
  // .toString() == [2, 4, 3, 2, 0].toString()
);