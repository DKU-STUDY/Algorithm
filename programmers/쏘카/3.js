function solution(r, delivery) {
  const memo = new Map();
  const maxTime = delivery.reduce((max, [time]) => Math.max(max, time), 0);
  let max = 0;

  const f = ([x, y], path, sumTip, time) => {
    if (time >= maxTime) {
      max = Math.max(sumTip, max);
      return
    }
    const nextPoints = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]];
    const before = path[path.length - 2];
    for (const [nextX, nextY] of nextPoints) {
      if (`${nextX},${nextY}` === before) continue;
      if (nextX >= r || nextX < 0 || nextY >= r || nextY < 0) continue;
      const [limit, tip] = delivery[nextY * r + nextX];
      const addTip = time <= limit && path.indexOf(`${nextX},${nextY}`) === -1 ? tip : 0;
      f([nextX, nextY], [ ...path, `${nextX},${nextY}` ],sumTip + addTip, time + 1);
    }
  }

  f([0, 0], ['0,0'], delivery[0][1], 0);

  return max
}

console.log(
  solution(3, [[1, 5],[8, 3],[4, 2],[2, 3],[3, 1],[3, 2],[4, 2],[5, 2],[4, 1]]) === 17,
  solution(4, [[1,10],[8, 1],[8, 1],[3, 100],[8, 1],[8, 1],[8, 1],[8, 1],[8, 1],[8, 1],[8, 1],[8, 1],[9, 100],[8, 1],[8, 1],[8, 1]]) === 217
)