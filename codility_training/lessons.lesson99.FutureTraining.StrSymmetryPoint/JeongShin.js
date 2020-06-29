function solution(S) {
    const len = S.length;
    if (!len)
        return -1;
    const mid = ~~(len / 2);
    const left = S.slice(0, mid);
    const right = [...S.slice(mid + 1)].reverse().join("");
    if (left === right)
        return mid;
    return -1;
}