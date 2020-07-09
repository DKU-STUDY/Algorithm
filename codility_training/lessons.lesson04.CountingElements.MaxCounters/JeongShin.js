/*스스로 작성한코드*/

function solution(N, A) {
    if (!A || N === 0) return;
    const arr = new Array(N+1).fill(0); // arr[0]에는 max 값을 넣는데 사용하였습니다.
    for (const val of A){
        if (val===N+1){
            //fill 함수가 arr 를 iterate하기 때문에 이 부분에서 performance가 저하 된다.
            arr.fill(arr[0]);
        }
        else {
            if (arr[0]<++arr[val])
                arr[0]=arr[val];
        }
    }
    return arr.slice(1);
}
solution(5, [3,4,4,6,1,4,4]);

/*@JunilHwang 형의 코드를 참고하여 작성한 코드*/

function solution(N, A) {
    if (!A || N === 0) return;
    const counters = new Array(N).fill(0);
    let prev_max = 0, curr_max = 0;
    for (const val of A) {
        if (1 <= val && val <= N) {
            let idx = val - 1;
            counters[idx] = Math.max(counters[idx], prev_max)
            counters[idx]++;
            curr_max = Math.max(curr_max, counters[idx]);
        } else if (val === N + 1) {
            prev_max = curr_max;
        }
    }
    return counters.map(el => el < prev_max ? prev_max : el);
}

let counters = solution(5, [3, 4, 4, 6, 1, 4, 4, 6, 4, 5]);
console.log(counters);