/**
 * https://programmers.co.kr/learn/courses/30/lessons/42583?language=javascript
 * @param bridge_length 다리의 길이
 * @param weight 다리가 견딜 수 있는 무게
 * @param truck_weights 트럭의 무게를 담은 배열
 * @return 모든 트럭이 다리를 건너기 위해 걸리는 최소 시간
 * 다리는 1초에 한칸씩 이동할 수 있다.
 *
 bridge_length는 1 이상 10,000 이하입니다.
 weight는 1 이상 10,000 이하입니다.
 truck_weights의 길이는 1 이상 10,000 이하입니다.
 모든 트럭의 무게는 1 이상 weight 이하입니다.

 */

/*
 * solution2 에서
 *     const targetTruck = standing[0];
 standing.shift();
 와 반대로
 * const targetTruck = standing[standing.length - 1];
 standing.pop();
 거꾸로 순회해도 거의 비슷한 시간과 정답을 보였다.
 * */

function solution(bridge_length, weight, truck_weights) {
  if (bridge_length === 1) return truck_weights.length + 1;

  // 마지막 truck 이 건널 때 소요되는 시간으로 초기화를 해준다.
  let time = bridge_length;

  // 대기중인 트럭의 배열
  const standing = [...truck_weights];

  // 다리위의 트럭의 배열
  const bridge = [];

  // 다리 위의 트럭의 총 무게
  let bridgeWeight = 0;

  // 대기 중인 트럭이 모두 다리위에 올라갈 때 까지 반복한다
  while (standing.length !== 0) {
    const targetTruck = standing[0];

    // bridge 가 꽉찬 시점에서 pop 을 실행한다는 점이 solution2 와 다르다.
    if (bridge.length === bridge_length) {
      bridgeWeight -= bridge.pop();
    }

    let put = 0;

    // 다리 위에 올라갈 수 있다면 다리위의 무게에 합산하고, 대기중인 트럭 배열에서 해당 트럭을 제거한다.
    if (bridgeWeight + targetTruck <= weight) {
      put = targetTruck;
      standing.shift();
    }

    // 다리위에 트럭을 올린다.
    bridge.unshift(put);
    bridgeWeight += put;
    time += 1;
  }
  return time;
}
/* solution 2 보다 살짝 빠르다.
 테스트 1 〉	통과 (0.72ms, 29.9MB)
 테스트 2 〉	통과 (33.79ms, 32.4MB)
 테스트 3 〉	통과 (0.08ms, 30MB)
 테스트 4 〉	통과 (9.19ms, 32.7MB)
 테스트 5 〉	통과 (222.68ms, 32.8MB)
 테스트 6 〉	통과 (33.44ms, 32.4MB)
 테스트 7 〉	통과 (0.67ms, 29.9MB)
 테스트 8 〉	통과 (0.11ms, 29.8MB)
 테스트 9 〉	통과 (3.43ms, 32.6MB)
 테스트 10 〉	통과 (0.22ms, 30.1MB)
 테스트 11 〉	통과 (0.10ms, 30.1MB)
 테스트 12 〉	통과 (0.32ms, 30MB)
 테스트 13 〉	통과 (0.82ms, 30.1MB)
 테스트 14 〉	통과 (0.09ms, 30MB)
 */

function solution2(bridge_length, weight, truck_weights) {
  if (bridge_length === 1) return truck_weights.length + 1;
  let time = 0;
  const standing = [...truck_weights];
  const bridge = new Array(bridge_length).fill(0);
  let bridgeWeight = 0;

  while (standing.length !== 0) {
    const targetTruck = standing[0];

    const pop = bridge.pop();
    bridgeWeight -= pop;

    let put = 0;
    if (bridgeWeight + targetTruck <= weight) {
      put = targetTruck;
      standing.shift();
    }
    bridge.unshift(put);
    bridgeWeight += put;
    time += 1;
  }
  return time + bridge_length;
}
/*
 테스트 1 〉	통과 (0.72ms, 30MB)
 테스트 2 〉	통과 (37.70ms, 32.7MB)
 테스트 3 〉	통과 (0.07ms, 30MB)
 테스트 4 〉	통과 (9.02ms, 32.8MB)
 테스트 5 〉	통과 (223.29ms, 32.7MB)
 테스트 6 〉	통과 (31.52ms, 32.6MB)
 테스트 7 〉	통과 (0.69ms, 29.9MB)
 테스트 8 〉	통과 (0.21ms, 30MB)
 테스트 9 〉	통과 (3.40ms, 32.4MB)
 테스트 10 〉	통과 (0.24ms, 30MB)
 테스트 11 〉	통과 (0.09ms, 29.9MB)
 테스트 12 〉	통과 (0.30ms, 30.1MB)
 테스트 13 〉	통과 (1.02ms, 29.7MB)
 테스트 14 〉	통과 (0.09ms, 29.9MB)
 * */

console.log(solution(2, 10, [7, 4, 5, 6]) === 8);
console.log(solution(2, 10, [10, 4, 5, 6]) === 8);
console.log(solution(2, 10, [7]) === 3);
console.log(solution(100, 100, [10]) === 101);
console.log(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) === 110);
console.log(solution(5, 6, [1, 2, 3, 1, 2]) == 12);
console.log(solution(1, 2, [1, 1, 1]) === 4);
console.log(solution(1, 1, [1, 1, 1]) === 4);
console.log(solution(4, 2, [1, 1, 1, 1]) === 10);
console.log(solution(3, 3, [1, 1, 1]) === 6);
console.log(solution(3, 1, [1, 1, 1]) === 10);
console.log(solution(5, 5, [1, 1, 1, 1, 1, 2, 2]) === 14);
console.log(solution(7, 7, [1, 1, 1, 1, 1, 3, 3]) === 18);
console.log(solution(5, 5, [1, 1, 1, 1, 1, 2, 2, 2, 2]) === 19);
console.log(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]) === 19);

// 옛날에 푼 것
function solution2(bridge_length, weight, truck_weights) {
  let cnt = 0, cur_weight = 0;
  let bridge_in_truck = [...new Array(bridge_length)].fill(0);

  while (truck_weights.length) {
    let J = truck_weights.shift();
    let flag = false;
    while (cur_weight + J > weight) {
      let p = bridge_in_truck.pop();
      cur_weight = cur_weight - p;
      if (cur_weight < weight) {
        bridge_in_truck.unshift(J);
        cnt++;
        flag = true;
        continue;
      } else {
        bridge_in_truck.unshift(0);
        cnt++;

      }
      cnt++;
    }// 다리에 건널 수 있나 판별?
    if (flag === false) {
      let p = bridge_in_truck.pop();
      bridge_in_truck.unshift(J);
      cur_weight = cur_weight - p + J;
      cnt++;
    }
  }
  return cnt + bridge_length;
}