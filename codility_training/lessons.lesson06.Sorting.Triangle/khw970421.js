//sort후에 가장가까운3개의 값을 길이계산했을 때 가능하면 1리턴 아니면 0리턴
//정확성 효율성 문제x

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    A.sort((a,b)=>a-b);
    for(let i=0;i<A.length-2;i++){
        if(A[i]+A[i+1]>A[i+2])
            return 1;
    }
    return 0;
}