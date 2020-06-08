function solution(A) {
  return !(A.sort((a, b) => a - b).find((v, k) => v - 1 !== k)) * 1
}

function solution2(A) {
  return (A.sort((a,b)=>a-b).reduce(([acc, count], val) => {
    if(val - acc !== 1) return [-1, 0];
    count++;
    return [val,count];
  }, [ 0, 0 ])[1] === A.length) * 1
}

console.log(
  solution2( [4, 1, 3, 2]) === 1,
  solution2([4, 1, 3]) === 0,
)