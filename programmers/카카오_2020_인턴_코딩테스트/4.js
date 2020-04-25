function solution(k, room_number) {
  const root = {
    min: 0,
    arr: [],
    max: 0,
    next: null
  }
  const listFind = k => {
    console.log('\nroot', root)

    if (root.max === 0) {
      root.min = k
      root.arr = [k]
      root.max = k + 1
      root.next = null
      return k
    }

    let node = root

    while (true) {
      if (node.min <= k && k <= node.max) break

      if (node.next === null) {
        node.next = {
          min: k,
          arr: [k],
          max: k + 1,
          next: null
        }
        return k
      }

      node = node.next
    }

    console.log('Selected Node', k, node)

    if (node.arr.indexOf(k) === -1) {
      node.arr.push(k)
      if (k === node.max) node.max += 1
      return k
    }

    let max = node.max
    node.max += 1
    node.arr.push(max)

    if (node.next !== null && node.max === node.next.min) {
      node.arr.push(...node.next.arr)
      node.max = node.next.max
      node.next = node.next.next
    }

    return max

}

  const arr = room_number.map(v => listFind(v))
  console.log(arr)
  return arr
}


// console.log(solution(10, [1,3,4,1,3,1]).toString() === [1,3,4,2,5,6].toString())
// console.log(solution(10, [1,1,1,3,3,3]).toString() === [1,2,3,4,5,6].toString())
// console.log(solution(200000, [1,1,1,10,10,10]).toString() === [1,2,3,10,11,12].toString())
const max = 10 ** 10
console.log(solution(200000, [1,1,1,max,max,max]).toString() === [1,2,3,max,max+1,max+2].toString())