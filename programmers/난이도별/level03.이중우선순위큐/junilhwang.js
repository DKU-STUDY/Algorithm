// https://programmers.co.kr/learn/courses/30/lessons/42628
class Heap {
  constructor () { this.v = [] }
  push (n) {
    this.v.push(n)
    this.v.sort((a, b) => a - b)
  }
  pop (type) { type === 1 ? this.v.pop() : this.v.shift() }
  getMax (len = this.v.length) { return len ? this.v[len - 1] : 0 }
  getMin (len = this.v.length) { return len ? this.v[0] : 0 }
}

function solution (operations) {
  const heap = new Heap();
  operations.forEach(v => { const [command, n] = v.split(' '); command === 'I' ? heap.push(~~n) : heap.pop(n*1) })
  return [heap.getMax(), heap.getMin()];
}

console.log(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]), [0, 0])
console.log(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]), [333, -45])
// console.log(solution(["I 16", "D 1"]), [0,0])
// console.log(solution(["I 7", "I 5", "I -5", "D -1"]), [7,5])