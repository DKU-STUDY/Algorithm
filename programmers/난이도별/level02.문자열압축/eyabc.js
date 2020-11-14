const JSTestModule = require('/Users/ey/DKU/Algorithm/JSTestModule.js');

const getZippedLength = (unit, str, strLen) => {
    let zippedStr = '';
    let pos = unit, currStr = str.slice(0, unit), currRepeat = 1;
    const newStr = () =>
        ((currRepeat === 1) ? '' : currRepeat) + currStr;

    while (pos < strLen) {
        const nextStr = str.slice(pos, pos + unit);

        if (currStr === nextStr)
            currRepeat++;
        else {
            zippedStr += newStr();
            [currStr, currRepeat] = [nextStr, 1];
        }
        pos += unit;
    }
    zippedStr += newStr();

    return zippedStr.length;
};

function solution (s) {
    const strLen = s.length;
    const maxUnit = strLen / 2 + 1;
    let shortestLen = strLen;

    for (let unit = 1 ; unit < maxUnit ; unit++) {
        const zippedLen = getZippedLength(unit, s, strLen);
        shortestLen = Math.min(shortestLen, zippedLen);
    }
    return shortestLen;
}

JSTestModule('/Users/ey/DKU/Algorithm/programmers/카카오/문자열압축/test.json', solution);