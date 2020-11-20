function solution(s) {
    const len = s.length
    let max = 0
    for (let i = 0; i < len; i += 0.5) {
        const [leftIdx, rightIdx] = [Math.floor(i), Math.ceil(i)];
        let count = 0
        for (; count < len; count++) {
            const [left, right] = [s[leftIdx - count], s[rightIdx + count]]
            if (!left || !right || left !== right)
                break
        }
        max = Math.max(max, count * 2 - (leftIdx === rightIdx))
    }
    return max
}