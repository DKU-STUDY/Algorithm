function solution (N, M, map) {
  let max = 0;

  const f = ([x, y], bag) => {
    console.log({x, y, bag});

    if (x < N - 1 && y < M - 1 ) {
      f([x + 1, y], bag + map[x][y]);
      f([x, y + 1], bag + map[x][y]);
    } else if (x === N - 1 && y < M - 1) {
      f([x, y + 1], bag + map[x][y + 1]);
    } else if (y === M - 1 && x < N - 1) {
      f([x + 1, y], bag + map[x + 1][y]);
    }
    max = Math.max(bag, max);
    return;
  };

  f([0, 0], map[0][0]);
  return max;
}


console.log(solution(1, 2, [[0, 1]]) === 1);
console.log(solution(3,	3,	[[2,0,0],[2,0,0],[2,2,2]]) ===	10)


