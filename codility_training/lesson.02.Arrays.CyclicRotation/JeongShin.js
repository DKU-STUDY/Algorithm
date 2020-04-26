function solution(A, K) {
    return arr.slice(A.length-K).concat(arr.slice(0,A.length-K));
}
var arr=[1,2,3,4];
let arr2=solution(arr, 3);

console.log(arr2);