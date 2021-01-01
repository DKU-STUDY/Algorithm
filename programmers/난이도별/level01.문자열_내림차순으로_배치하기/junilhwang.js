function solution (s) {
  return [ ...s ].sort((a, b) => a < b ? 1 : -1).join('')
}

require('./test.json').forEach(({ input, output }) => console.log(solution(...input) === output))