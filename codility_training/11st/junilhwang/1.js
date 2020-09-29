function solution (S) {
  const map = {};
  for (const [k, v] of Object.entries(S)) {
    v.split('').forEach((c, position) => {
      const mapKey = `${c},${position}`;
      map[mapKey] = map[mapKey] || [];
      map[mapKey].push(k);
    })
  }
  for (const [k, v] of Object.entries(map)) {
    if (v.length === 1) continue;
    const z = k.split(',')[1];
    return [ ...v, z ].map(Number);
  }
  return [];
}

console.log(solution(["abc", "bca", "dbe"]), [0, 2, 1]);
console.log(solution(["zzzz", "ferz", "zdsr", "fgtd"]), [0, 1, 3]);
console.log(solution(["gr", "sd", "rg"]), []);
console.log(solution(["bdafg", "ceagi"]), [0, 1, 2]);