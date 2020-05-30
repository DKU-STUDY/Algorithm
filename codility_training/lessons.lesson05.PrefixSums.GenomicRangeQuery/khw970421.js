//정확성은 만족하나 효율성에서 문제
function solution(S, P, Q) {
    let k=[];
    const o=[];
    const q=['A','C','G','T'];
    for(let i=0;i<P.length;i++){
        k=S.split('').slice(P[i], Q[i]+1);
        if(k.sort()[0]=='A')
            o.push(1);
        else if(k.sort()[0]=='C')
            o.push(2);
        else if(k.sort()[0]=='G')
            o.push(3);
        else
            o.push(4);
    }

    return o;
}


//reduce사용했으나 위와같이 효율성문제
function solution(S, P, Q) {
    let k=[];
    const o=[];
    const q=['A','C','G','T'];
    for(let i=0;i<P.length;i++){
        k=S.split('').slice(P[i], Q[i]+1);

        q.reduce(function(acc,current,index){
            if(current==k.sort()[0])
                o.push(index+1);
        },0)
    }
    return o;
}


