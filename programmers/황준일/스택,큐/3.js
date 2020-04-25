/*
  여러 개의 쇠막대기를 레이저로 절단하려고 합니다.
  효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고,
  레이저를 위에서 수직으로 발사하여 쇠막대기들을 자릅니다.
  쇠막대기와 레이저의 배치는 다음 조건을 만족합니다.

  - 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있습니다.
  - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓습니다.
  - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재합니다.
  - 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않습니다.
*/
function solution(arrangement) {
  const str = arrangement.replace(/\(\)/gi, 'l')
  const stack = [] 
  let num = 0
  for (let i = 0, len = str.length; i < len; i++) {
    const c = str.charAt(i)
    switch (c) {
      case '(' : stack.push('bar'); break;
      case ')' : stack.pop(), num += 1; break;
      case 'l' : num += stack.length; break;
    }
  }
  return num;
}

console.log(solution("()(((()())(())()))(())"))