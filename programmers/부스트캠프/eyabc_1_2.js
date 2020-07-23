function solution (arrayA, arrayB) {
  const ASet = arrayA.reduce((arr, v) => {
    if (arr.indexOf(v) === -1) arr.push(v);
    return arr;
  }, []);

  const BSet = arrayB.reduce((arr, v) => {
    if (arr.indexOf(v) === -1) arr.push(v);
    return arr;
  }, []);

  const sum = ASet.reduce((arr, v) => {
    if (arr.indexOf(v) === -1) arr.push(v);
    return arr;
  }, [...BSet]);

  const diff = BSet.reduce((arr, v) => {
    const idx = arr.indexOf(v);
    if (idx !== -1) {
      arr.splice(idx, 1);
    }
    ;
    return arr;
  }, [...ASet]);

  const same = BSet.reduce((arr, v) => {
    const idx = ASet.indexOf(v);
    if (idx !== -1) {
      arr.push(v);
    }
    ;
    return arr;
  }, []);

  return [ASet.length, BSet.length, sum.length, diff.length, same.length];
}

// '[a의 set, b의 셋, ab 합,ab 차, ab교]';

console.log(
  solution([1, 2, 3, 2], [1, 3]),
  solution([2, 3, 4, 3, 5], [1, 6, 7]),
);