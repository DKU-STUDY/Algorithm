/*
  주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
  숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
  nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의
  개수를 return 하도록 solution 함수를 완성해주세요.

  제한사항
  nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
  nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
*/

function solution(nums) {
  let cnt = 0
  let len = nums.length
  for (let start = 0; start < len - 2; start++) {
    for (let i = start + 1; i < len - 1; i++) {
      for (let j = i + 1; j < len; j++) {
        if (check(nums[start], nums[i], nums[j])) cnt += 1
      } 
    }
  }
  return cnt
}

function check (num1, num2, num3) {
  const num = num1 + num2 + num3
  if (num < 3 || num % 2 === 0) return false
  for (let i = 3; i < num / 2; i++) {
    if (num % i === 0) return false
  }
  return true
}

console.log(solution([1,2,3,4]))
console.log(solution([1,2,7,6,4]))