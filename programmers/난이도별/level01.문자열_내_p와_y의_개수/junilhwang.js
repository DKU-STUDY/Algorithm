function solution(s){
    const str = [ ...s ]
    return str.filter(v => ['p', 'P'].indexOf(v) !== -1).length === str.filter(v => ['y', 'Y'].indexOf(v) !== -1).length;
}

require('./test.json').forEach(({ input, output }) => console.log(solution(...input) === output))