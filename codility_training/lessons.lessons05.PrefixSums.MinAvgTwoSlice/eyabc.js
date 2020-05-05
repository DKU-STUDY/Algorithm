let min = [Infinity, Infinity];
let num = 1;
function solution(A) {
  if (A.length === 2) return 0;
  num++;
  min = A.reduce((oldValue, v, k) => {
    if(!A[k+num-1]) return oldValue;
    const newValue = v + A[k+1] + (num === 3 ? A[k+2] : 0);
    const lastValue = Math.min(oldValue[0], newValue / num);
    return [lastValue, lastValue !== oldValue[0] ? k : oldValue[1]];
  }, min);

  if (num === 2) solution(A);
  return min[1];
}

function solution2(A) {
  if (A.length === 2) return 0;

  let min = A.reduce(([ min, minIdx ], v, k) => {
    if(!A[k+1]) return oldValue;
    const newValue = v + A[k+1];
    const lastValue = Math.min(min, newValue / 2);
    return [lastValue, lastValue !== oldValue[0] ? k : oldValue[1]];
  }, [Infinity, Infinity]);

  min = A.reduce((oldValue, v, k) => {
    if(!A[k+2]) return oldValue;
    const newValue = v + A[k+1] + A[k+2];
    const lastValue = Math.min(oldValue[0], newValue / 3);
    return [lastValue, lastValue !== oldValue[0] ? k : oldValue[1]];
  }, min);
  return min[1];
}

console.log(
  solution([4, 2, 2, 5, 1, 5, 8]) === 1,
  solution([-10000, -10000]) === 0,
  solution([-3, -5, -8, -4, -10]) === 2,
);
