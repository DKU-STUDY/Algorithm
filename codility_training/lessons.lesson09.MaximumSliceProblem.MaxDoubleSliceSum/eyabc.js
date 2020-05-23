/* @JeongShing 님꺼, MaximumSliceProblem 문제랑 prefixSums 의 문제를 합쳐서 푼것같다 .*/
function solution(A) {
  const len = A.length;
  const lArr = [], rArr=[];

  for (let i = 1; i < len; i++)
    lArr[i] = Math.max(0, (lArr[i - 1] || 0) + A[i]);

  for(let i = len-2; i >= 1; i--)
    rArr[i] = Math.max(0, (rArr[i+1] || 0) + A[i]);

  let maxSum = 0;

  for(let i = 1; i < len-1; i++)
    maxSum = Math.max(maxSum, (lArr[i-1] || 0) + (rArr[i+1] || 0));

  return maxSum;
}

console.log(solution([5, -7, 3, 5, -2, 4, -1]))
console.log(solution([3, 2, 6, -1, 4, 5, -1, 2]))

