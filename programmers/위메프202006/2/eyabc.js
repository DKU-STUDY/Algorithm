function solution(N, M, arr) {
  let min = Infinity;
  const pos = arr.reduce((pos, v, x) => {
    v.forEach((w, y) => {
      if (w) pos.push([x, y]);
    });
    return pos;
  }, []);

  if (pos.length < 2) return 0.0;

  for (let i = 0; i < pos.length; i++) {
    for (let j = i + 1; j < pos.length; j++) {
      const dist = +Math.sqrt((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2).toFixed(2);
      if (min > dist) min = dist;
    }
  }
  return min;
}

console.log(solution(3,	4,	[[1,0,0,0],[0,0,0,0],[0,0,0,1]]) === 3.61);
console.log(solution(3,	4,	[[1,1,0,0],[0,0,0,0],[0,0,0,1]]) === 1.0);