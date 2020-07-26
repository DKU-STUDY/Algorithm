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

//다른 코드 참조해서 작성한 코드
function solution(A) {
    let len = A.length;
    let max = -Infinity;        //max는 최대로 작은값 기준
    let min = Infinity;         //min은 최대로 큰 값 기준

    if (len == 0 || len == 1)
        return 0;

    for (let i = 0 ; i < len ; i++)
    {
        min = Math.min(A[i], min);          //현재 A[i]위치에서 제일 작은 값을 기준으로
        max = Math.max(max, A[i]-min);      //A[i]위치에서와 가장작은 min의 차이와 그전에 가장 컸던 max를 비교
    }
    return max;
}

//피드백 후 작성한 코드

function solution(A) {
    let len = A.length;
    let max = -Infinity;        //max는 최대로 작은값 기준
    let min = Infinity;         //min은 최대로 큰 값 기준

    if (len < 2)
        return 0;

    return A.reduce(([min, max], v) => {
        min = Math.min(v, min);
        max = Math.max(max, v - min);
        return [min ,max];
    },[min,max])[1];
}

