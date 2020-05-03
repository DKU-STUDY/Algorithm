function solution(S, P, Q) {
    const pLen = P.length;
    const sLen = S.length;
    const arr = [];
    const sString = S.split('').map(v => {
         switch (v) {
            case 'A' : return 1;
            case 'C' : return 2;
            case 'G' : return 3;
            case 'T' : return 4;
        }
    })

    for(let i = 0; i < pLen; i++) {
        const start = P[i];
        const end = Q[i];
        if(start === end) arr.push(sString[start])
        else {
            arr.push(Math.min(...sString.slice(P[i], Q[i])));
        }
    }
    return arr
}
임시저장
