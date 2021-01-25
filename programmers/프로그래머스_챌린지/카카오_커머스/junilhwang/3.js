function solution(next_student) {
  const pathMap = next_student.map((v, k) => {
    const arr = Array(next_student.length).fill(0);
    arr[k] = 1;
    return arr;
  });
  const nextStudent = next_student.map(v => v - 1);

  const circle = (start) => {
    let now = start;
    let next;
    while (true) {
      next = nextStudent[now];
      if (next === start || next === -1) return;
      if (pathMap[start][next]) return;
      pathMap[now][next] = 1;
      pathMap[start][next] = 1;
      now = nextStudent[now];
    }
  }

  nextStudent.forEach((v, k) => circle(k));

  const arr = pathMap.map(arr => arr.reduce((sum, v) => sum + v, 0));
  const max = Math.max(...arr);

  return arr.lastIndexOf(max) + 1;
}

console.log(
  [solution([5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2]), 3],
  [solution([6, 10, 8, 5, 8, 10, 5, 1, 6, 7]), 9]
);
