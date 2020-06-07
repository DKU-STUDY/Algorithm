//정확성은 만족하나 효율성에서 문제
function solution(S, P, Q) {
    let k=[];
    const o=[];
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
    for(let i=0;i<P.length;i++){
        k=S.split('').slice(P[i], Q[i]+1);

        q.reduce(function(acc,current,index){
            if(current==k.sort()[0])
                o.push(index+1);
        },0)
    }
    return o;
}


//준일이형의 피드백 코드
function solution(S, P, Q) {
const o=[];
for(let i=0, len = P.length; i< len; i++){
    const temp = S.substring(P[i], Q[i]+1);
    for (let j = 0, tLen = temp.length; j < tLen; j++) {
        if ( temp.indexOf('A') !== -1 ) { o.push(1); break }
        if ( temp.indexOf('C') !== -1 ) { o.push(2); break }
        if ( temp.indexOf('G') !== -1 ) { o.push(3); break }
        if ( temp.indexOf('T') !== -1 ) { o.push(4); break }
    }
}
return o;
}

