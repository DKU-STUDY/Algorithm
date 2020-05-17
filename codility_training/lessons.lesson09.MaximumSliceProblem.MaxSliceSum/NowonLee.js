function solution(A) {
  if(A.length===1) return A[0]
  return A.reduce(([loc, glob], el, idx) => {
    if(idx > 0){
      loc = Math.max(el, loc + el); 
      glob = Math.max(loc, glob);
    }
    return [loc, glob];
  },[A[0],A[0]])[1]
}
  

console.log(solution([3,2,-6,4,0]) === 5)
