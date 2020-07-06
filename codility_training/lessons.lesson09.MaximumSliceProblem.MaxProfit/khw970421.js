//정확도 100 효율성 75

function solution(A) {
    let max=0;
    const A_size=A.length;
    for(let i=0;i<A_size;i++){
        for(let j=i+1;j<A_size;j++){
            if(A[j]<A[i])                   //이전값보다 작으면 이윤이 없으므로 아예 시도 x
                break;
            max=Math.max(A[j]-A[i],max);
        }
    }
    return max;                             //가장큰 이윤을 return
}

//정확도 100 효율성 100
function solution(A) {
    let max=0;
    const A_size=A.length;
    for(let i=0;i<A_size;i++){
        for(let j=i+1;j<A_size;j++){
            if(A[j]<=A[i])                   //이전값보다 작으면 이윤이 없으므로 아예 시도 x
                break;
            max=Math.max(A[j]-A[i],max);
        }
    }
    return max;                             //가장큰 이윤을 return
}

// 큰 양의 반복문에서 효율성 문제가 나타났는데 생각해보니 굳이 A[j]가 A[i]랑 같은것도 필요할까싶어(이윤이 0이니 결국) 없애니 효율성 문제 해결