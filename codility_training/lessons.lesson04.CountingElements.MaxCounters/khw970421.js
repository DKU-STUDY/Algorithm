//large size time out
function solution(N, A) {
    const arrNumber = new Array().fill(0); //배열선언
    let max=0;
    for(let i=0;i<N;i++){
        arrNumber[i]=0;
    }
    A.reduce(function(acc,value){
        if(value>N){
            arrNumber.fill(max);
        }
        else{
            arrNumber[value-1]++;
            max=Math.max(arrNumber[value-1],max);
        }
    },0);
    return arrNumber;
}
//준일형 소스코드 이해
function solution1(N, A) {
    let max = 0, Save = 0;
    const arr = new Array(N).fill(0);
    for(const v of A) {                             //A의 배열값을 v에 저장해 실행
        if (v > N) Save = max;                      //배열값이 N 한계치보다 크다면 실행
        else {
            arr[v-1] = Math.max(arr[v-1], Save) + 1;        //Save랑 arr[v-1]의 값을 비교해 큰값에 1을 더한것을 저장
            max = Math.max(arr[v-1], max);                  //변한값과 max 비교해 큰값을 max에 저장
        }
    }
    return arr.map(v => Math.max(v, Save));                 //arr의 배열값중에 Save보다 작은값은 Save로 채우기
}

console.log(solution(5, [3, 4, 4, 6, 1, 4, 4]).toString()=== [3, 2, 2, 4, 2].toString());