/*제가 작성한 코드*/
function solution(A) {
    const len = A.length;
    const arr = [];
    for (let i = 0; i < len; i++) {
        if (arr[A[i] - 1])
            return 0;
        else
            arr[A[i] - 1] = true
    }

    for (const val of arr) {
        if (val === undefined)
            return 0
    }
    return 1;
}

console.log(solution([1, 2, 3, 4]));

/*@JunilHwang 코드 참고*/
function solution2(A){
    /* 1.배열 Sort
    * 2. 배열 내 모든 값과 index를 비교 하나씩 비교 (A.find()는 찾지 못할시 undefined를 반환)
    * 3. 형 변환 후 return;
    * */
   return !(A.sort((a,b) => a-b).find((val , idx)=> val - 1 !== idx))*1;
}
