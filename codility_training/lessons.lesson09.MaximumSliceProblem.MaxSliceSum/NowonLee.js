function solution(A) {
  if(A.length===1) return A[0]
  else {
      var localVar = A[0]
      var globalVar = A[0]
      A.forEach((el, index) => {
          if(index!==0){
              localVar = Math.max(el, localVar + el)
              globalVar = Math.max(localVar, globalVar)
      
          }
      })
      return globalVar
  }
}

console.log(solution([3,2,-6,4,0]) === 5)
