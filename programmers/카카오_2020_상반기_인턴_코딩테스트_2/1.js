function solution(numbers, hand) {
  const table = {
    '1': { value: [0, 0], type: 'L' },
    '2': { value: [0, 1], type: 'C' },
    '3': { value: [0, 2], type: 'R' },
    '4': { value: [1, 0], type: 'L' },
    '5': { value: [1, 1], type: 'C' },
    '6': { value: [1, 2], type: 'R' },
    '7': { value: [2, 0], type: 'L' },
    '8': { value: [2, 1], type: 'C' },
    '9': { value: [2, 2], type: 'R' },
    '*': { value: [3, 0], type: 'L' },
    '0': { value: [3, 1], type: 'C' },
    '#': { value: [3, 2], type: 'R' },
  }
  const pos = [[3, 0], [3, 2]]

  const result = numbers.map(n => {
    const { type, value } = table[n]
    switch(type) {
      case 'L': pos[0] = [ ...value ]; return 'L';
      case 'R': pos[1] = [ ...value ]; return 'R';
      default:
        const leftType = Math.abs((pos[0][0] - value[0]) - (pos[0][1] - value[1]))
        const rightType = Math.abs((pos[1][0] - value[0]) - (pos[1][1] - value[1]))
        if (leftType > rightType) {
          pos[0] = [ ...value ]
          return 'L'
        }
        if (rightType > leftType) {
          pos[1] = [ ...value ]
          return 'R'
        }

        const chk = hand === 'left'
        pos[chk ? 0 : 1] = [ ...value ]
        return chk ? 'L' : 'R'
    }
  }).join('')

  console.log(result)

  var answer = '';
  return answer;
}

console.log(
  solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") === "LRLLLRLLRRL",
  solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") === "LRLLRRLLLRR",
  solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") === "LLRLLRLLRL",
)