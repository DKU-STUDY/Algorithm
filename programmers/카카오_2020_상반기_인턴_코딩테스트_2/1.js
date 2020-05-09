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
  const pos = ['*', '#']

  const answer = numbers.map(n => {
    console.log('n', n)
    const { type, value } = table[n]
    switch(type) {
      case 'L': pos[0] = n; return 'L';
      case 'R': pos[1] = n; return 'R';
      default:
        const left = table[pos[0]].value
        const right = table[pos[1]].value
        const leftType = Math.abs(Math.abs(left[0] - value[0]) + Math.abs(left[1] - value[1])) ** 2
        const rightType = Math.abs(Math.abs(right[0] - value[0]) + Math.abs(right[1] - value[1])) ** 2
        if (leftType < rightType) {
          pos[0] = n; return 'L'
        }
        if (rightType < leftType) {
          pos[1] = n; return 'R'
        }

        const chk = hand === 'left'
        pos[chk ? 0 : 1] = n
        return chk ? 'L' : 'R'
    }
  }).join('')

  console.log(answer)

  return answer;
}

console.log(
  solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") === "LRLLLRLLRRL",
  solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") === "LRLLRRLLLRR",
  solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") === "LLRLLRLLRL",
)