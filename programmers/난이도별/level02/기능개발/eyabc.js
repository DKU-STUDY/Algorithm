const COMPLETE = 100;

const deploy = (speeds) => ({ cnt, deployDay, result }, item, k) => {
  const remain = COMPLETE - item;
  const days = Math.ceil(remain / speeds[k]);

  // 시작
  if (k === 0) {
    deployDay = days;
    cnt += 1;
  }

  else if (days <= deployDay) {
    cnt += 1;
  }

  else if (days > deployDay) {
    result.push(cnt);
    cnt = 1;
    deployDay = days;
  }

  // 끝
  if (k === speeds.length - 1) {
    result.push(cnt);
  }

  return { cnt, deployDay, result };
};

function solution (progresses, speeds) {
  const init = {
    cnt: 0,
    deployDay: 0,
    result: [],
  };
  return progresses.reduce(deploy(speeds), init).result;
}

console.log(solution([93, 30, 55], [1, 30, 5]) === [2, 1]);
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) === [1, 3, 2]);


// 옛날에 푼 것
function solution2 (progresses, speeds) {
  var answer = [];
  while (speeds.length > 0) {
    // 개발
    for (let i in speeds) {
      if (progresses[i] < 100) {
        progresses[i] += speeds[i];
      }
    }

    // 배포
    let deploy_count = 0;
    while (progresses[0] >= 100) {
      progresses.shift();
      speeds.shift();
      deploy_count++;
    }
    if (deploy_count > 0) {
      answer.push(deploy_count);
    }
  }

  return answer;
}