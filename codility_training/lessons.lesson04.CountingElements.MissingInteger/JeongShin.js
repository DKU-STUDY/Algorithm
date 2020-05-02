function solution(A) {
    const set = Array.from(new Set(A)).sort((a,b)=> a-b);
    /*const set = Array.from(new Set(A).sort() -> 로 하면 제대로 오름차순 정렬이 안되더라고요.
    * 제가 알기론 int값을 포함한 array는 자동으로 오름차순 sort 하는거로 알고 있는데 혹시 시는분 코드 리뷰 부탁드려요*/
    const len = set.length;
    if (len === 0)
        return 1;
    let missing = 1;
    for (const val of set) {
        //missing보다 작은 val는 무시
        if (val >= missing) {
            if (val - missing !== 0)
                return missing;
            else
                missing++;
        }
    }
    return missing;
}
let sol1 = solution([0,1,2,4,3,5, 100]);
console.log(sol1);