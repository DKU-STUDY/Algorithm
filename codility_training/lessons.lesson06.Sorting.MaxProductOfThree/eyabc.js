function solution (A) {
  const aLen = A.length;
  A.sort((a, b) => a - b);
  return Math.max(A[0] * A[1] * A[aLen - 1], A[aLen - 1] * A[aLen - 2] * A[aLen - 3]);
}
/**
 * https://stackoverflow.com/questions/23487381/solve-maximum-product-of-three-array-elements-without-sorting
 * When we sort an array there are two possible options for the largest product
 * 1) The largest (the last) three elements
 * 2) Combination of two smallest and the largest elements
 * Logic of (1): Obvious
 * Logic of (2): A pair of negatives multiplied returns a positive, which in combination with
 * the largest positive element of the array can give the max outcome.
 * Therefore we return the max of options (1) and (2)
 */

console.log(
  solution([-3, 2, 2, -2, 5, 6]) === 60,
  solution([-5, 5, -5, 4]) === 125,
  solution([-4, -6, -3, 4, 5]) === 120,
  solution([4, 6, 3, 4, 5]) === 120,
);
