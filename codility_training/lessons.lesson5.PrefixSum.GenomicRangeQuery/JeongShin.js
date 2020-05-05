// Performance 측면에서 0 점 받았습니다 ㅜㅜ, 여러가지 방법으로 다 시도해봤지만 계속 0점이라
// @eyabc.js 님이 올리신 코드 보고 공부했습니다.

function solution(S, P, Q) {
    return Q.map((q, k) => {
        const val = S.slice(P[k], q+1);
        if(val.indexOf('A') !== -1) return 1;
        else if (val.indexOf('C') !== -1) return 2;
        else if (val.indexOf('G') !== -1) return 3;
        else if (val.indexOf('T') !== -1) return 4;
    });
}

/*제가 한 풀이 */
function solution2(S, P, Q) {
    const len = P.length;
    const arr = [];
    const map = char => {
        switch (char) {
            case 'A':
                return 1;
            case 'C':
                return 2;
            case 'G':
                return 3;
            case 'T':
                return 4;
        }
    };
    for (let i = 0; i < len; i++) {
        const s = Array.from(new Set(S.substring(P[i], Q[i] + 1)));
        s.sort((a, b) => a.charCodeAt(0)-b.charCodeAt(0));
        arr.push(map(s[0]));
    }
    return arr;
}

