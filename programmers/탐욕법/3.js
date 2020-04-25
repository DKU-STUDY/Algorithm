// https://programmers.co.kr/learn/courses/30/lessons/42883?language=javascript

function solution (nums, k) {
  const arr = Array.from(nums)
  const last = nums.length, len = last - k
  let left = 0, idx = 0, num = ""
  for (let i = 0; i < len; i++) {
    let max = nums[left]
    while (left <= k + i) {
      const n = nums[left]
      if (max < n) max = n, idx = left
      let nextLeft = -1, nextMax = 9
      while (nextMax > ~~max && nextLeft === -1) nextLeft = nums.indexOf(nextMax--, left+1)
      if (nextLeft === -1) break
      left = nextLeft < k + 1 ? nextLeft : left + 1
    }
    num += max, left = ++idx
  }
  return num
}

console.log(solution("1924", 2), "94")
console.log(solution("1231234", 3), "3234")
console.log(solution("4177252841", 4), "775841")