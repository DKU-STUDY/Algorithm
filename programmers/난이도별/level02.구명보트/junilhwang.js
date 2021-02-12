// 구명보트 : https://programmers.co.kr/learn/courses/30/lessons/42885?language=javascript
function solution(people, limit) {
  const nums = people.sort((a, b) => a - b)
  const len = nums.length, chk = nums.map(v => 0) 
  let cnt = 0, j = len - 1
  loop: for (let i = 0; i < len; i++) {
    if (chk[i]) continue
    chk[i] = 1
    for (; j > i; j--) {
      if (chk[j]) continue
      if (nums[i] + nums[j] === limit) {
        cnt += 1, chk[j] = 1; continue loop
      }
      if (nums[i] + nums[j] < limit) {
        cnt += 1, chk[j] = 1; continue loop
      }
    }
    cnt += 1
  }  
  return cnt;
}
console.log(solution([70, 50, 80, 50], 100), 	3)
console.log(solution([70, 80, 50], 100), 	3)
console.log(solution([50, 50, 60, 70], 100), 3)