/**
 * https://programmers.co.kr/learn/courses/30/lessons/12912?language=javascript
 * @param a 정수 / -10,000,000 이상 10,000,000 이하
 * @param b 정수 / -10,000,000 이상 10,000,000 이하
 * @return {number} a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수
 */
const sumDirectionAbs = (num) => {
  const abs = Math.abs(num);
  const direction = num > 0 ? 1 : -1;
  return [(abs + 1) * abs / 2, direction, abs];
};

function solution(a, b) {
  if ((a + b) === 0) return 0;

  const [aSum, aDirection, aAbs] = sumDirectionAbs(a);
  const [bSum, bDirection, bAbs] = sumDirectionAbs(b);

  if (aDirection !== bDirection)
    return aSum * aDirection + bSum * bDirection;

  let [diff, small] = [bSum - aSum, aAbs];

  if (diff < 0)
    [diff, small] = [aSum - bSum, bAbs];
  
  return (diff + small) * aDirection;
}

// 상민님 풀이
function solution2(a, b) {
  return ~~((a + b) * (Math.abs(a - b) + 1) / 2);
}


console.log(solution(3, 5) === 12);
console.log(solution(-3, -5) === -12);
console.log(solution(-3, 5) === 9); // -6 + 15 = 9
console.log(solution(3, -5) === -9);
console.log(solution(3, 3) === 3);
console.log(solution(5, 3) === 12);
console.log(solution(0, 0) === 0);
console.log(solution(0, 1) === 1);
console.log(solution(0, 1) === 1);
console.log(solution(1, 1) === 1);
console.log(solution(-1, 1) === 0);
