function solution(n, s) {
    let [q, r] = [Math.floor(s / n), s % n]
    if (q === 0)
        return [-1]
    const arr = new Array(n).fill(q);
    let i = n - 1;
    while (r > 0) {
        arr[i]++;
        r--;
        i--;
    }
    return arr
}