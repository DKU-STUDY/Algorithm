function solution(drum) {
  const rows = drum.length;
  const cols = drum[0].length;
  let count = 0;

  for (let i = 0; i < cols; i++) {
    let x = i;
    let y = 0;
    let breakCount = 0;
    while (y < cols) {
      const point = drum[y][x]
      if (point === '*') {
        breakCount += 1;
        y += 1;
        if (breakCount === 2) break;
      }
      switch (point) {
        case '#' : y += 1; break;
        case '>' : x += 1; break;
        case '<' : x -= 1; break;
      }
    }
    if (y === cols) count += 1;
  }

  return count;
}

console.log(
  solution(["######",">#*###","####*#","#<#>>#",">#*#*<","######"]) === 4
)