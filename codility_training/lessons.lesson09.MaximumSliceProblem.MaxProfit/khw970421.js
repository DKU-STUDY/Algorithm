//정확도 100 효율성 75

function solution(A) {
    let max=0;
    let count=0;
    let p=0;
    let A_size=A.length;
    for(let i=0;i<A_size;i++){
        for(let j=i+1;j<A_size;j++){
            if(A[j]<A[i])                   //이전값보다 작으면 이윤이 없으므로 아예 시도 x
                break;
            max=(count<max)?max:count;      //더큰 이윤을 계산

        }
    }
    return max;                             //가장큰 이윤을 return
}

