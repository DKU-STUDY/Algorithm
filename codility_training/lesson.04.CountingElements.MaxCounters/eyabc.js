
console.log(
  solution(5, [3, 4, 4, 6, 1, 4, 4]).toString() ===[3, 2, 2, 4, 2].toString()
);

/* timeout O(N^2)*/
function solution2(N, A) {
  const aLen = A.length;
  const arr = new Array(N).fill(0); // O(n)
  for (let i = 0; i < aLen; i++) { // O(n)
    const value = A[i];
    if (value > N) arr.fill(Math.max(...arr)); // O(n)
    else arr[value-1]++;
  }
  return arr;
}