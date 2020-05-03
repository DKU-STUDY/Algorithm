function solution (arr) {
  const len = arr.length
  const f = stack => {
    if (stack.length === len) {
      console.log(stack)
      return
    }
    arr.forEach(v => {
      if (stack.indexOf(v) === -1) f([ ...stack, v ])
    })
  }

  f([])
}

solution([1, 2, 3])
/* answer
  [ 1, 2, 3 ]
  [ 1, 3, 2 ]
  [ 2, 1, 3 ]
  [ 2, 3, 1 ]
  [ 3, 1, 2 ]
  [ 3, 2, 1 ]
*/