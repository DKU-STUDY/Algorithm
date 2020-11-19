const JSTestModule = require('/Users/ey/DKU/Algorithm/JSTestModule.js');


const isRightStr = (p) => {
    const stack = [p.charAt(0)],
        len = p.length;
    let pos = 1;

    while (pos < len) {
        const currChar = p.charAt(pos);
        const beforeChar = stack[stack.length - 1];

        (beforeChar === '(' && currChar === ')') ?
            stack.pop() :
            stack.push(currChar);
        pos++;
    }
    return !!(stack.length === 0);
};

const getUV = (equalStr) => {
    let uObj = {
        '(': 0,
        ')': 0,
    };
    let pos = 0;

    do {
        uObj[equalStr[pos]] += 1;
        pos++;
    } while (uObj['('] !== uObj[')']);

    const uLen = uObj['('] * 2;
    return [equalStr.slice(0, uLen), equalStr.slice(uLen, equalStr.length)];
};

const divideStr = (equalStr) => {
    // 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    const [u, v] = getUV(equalStr);

    // 나뉜 두 파트가 올바른 str 인지, 균형잡힌 str 인지 판별.
    const [isURight, isVRight] = [isRightStr(u), isRightStr(v)];

    let newV = '', newU = '';

    // 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if (isURight && !isVRight)
        newV = solution(v);

    if (!isURight) {
        const slicedU = [...u.slice(1, u.length - 1)].map(v => v === '(' ? ')' : '(').join('');
        newU = '(' + solution(v) + ')' + slicedU;
        return newU;
    }

    return (isURight ? u : newU) + (isVRight ? v : newV);
};

function solution (p) {
    // 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    return (p.length === 0) ? '' : divideStr(p);
}


JSTestModule('/Users/ey/DKU/Algorithm/programmers/카카오/괄호변환/test.json', solution);