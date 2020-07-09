function solution(S) {
    const alpha = /[A-Za-z]/g;
    const digit = /\d/g;
    const filtered = S.split(" ").filter(str => {
        // even # of alp
        const alp = str.match(alpha) !== null ? str.match(alpha).join("").length : 0;
        // odd # of dig
        const dig = str.match(digit) !== null ? str.match(digit).join("").length : 0;
        return !(alp % 2) && dig % 2 && ((alp + dig) === str.length)
    });
    if (!filtered[0])
        return -1;
    return filtered.reduce((max, curr) => Math.max(max, curr.length), 0);
}
