function solution(key, lock) {
  const len = key.length
  const turn = arr => {
    const temp = arr.map(v => arr.map(v2 => 0))
    for (let i = 0; i < len; i++) {
      for (let j = 0; j < len; j++) {
        temp[i][j] = arr[len - j - 1][i]
      }
    }
    return temp
  }
  const move = (arr, x = 0, y = 0) => {
    let temp = [...arr]
    if (y !== 0) {
      const absY = Math.abs(y)
      const [remove, insert] = y > 0 ? ['pop', 'unshift'] : ['shift', 'push']
      const z = arr.map(() => 0)
      for (let i = 0; i < absY; i++) {
        temp[remove]()
        temp[insert](z)
      }
    } else if (x !== 0) {
      const absX = Math.abs(x)
      const [remove, insert] = x > 0 ? ['pop', 'unshift'] : ['shift', 'push']
      for (let i = 0; i < len; i++) {
        for (let j = 0; j < absX; j++) {
          temp[i][remove]()
          temp[i][insert](0)
        }
      }
    }
    return temp
  }
  const chk = arr => {
    let cnt = 0
    console.log(arr, lock)
    for (let i = 0; i < len; i++) {
      for (let j = 0; j < len; j++) {
        if (arr[i][j] === lock[i][j]) return false
      }
    }
    return true
  }
  let temp = key
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < len; j++) {
      if (move(temp, j, 0) || move(temp, -j, 0)) return true
      for (let k = 1; k < len; k++) {
        if (move(temp, j, k) || move(temp, j, -k)) return true
        if (move(temp, -j, k) || move(temp, -j, -k)) return true
      }
    }
    temp = turn(temp)
  }
  return false
}

console.log(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]), true)