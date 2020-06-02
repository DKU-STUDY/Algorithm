/* Not finished
* */
function solution(K, M, A) {
    const dividable = (sum) => {
        let max = 0;
        const [k, m, acc] = A.reduce(([k, m, acc], curr) => {
            if ((m + 1) === M)
                return [k + 1, 0, 0];
            if (acc + curr > sum)
                return [k + 1, 1, curr];
            max = Math.max(acc + curr, max);
            return [k, m + 1, acc + curr];
        }, [0, 0, 0])
        return [k + (m !== 0) * 1, max];
    };

    let minSum = Math.max(...A)
    let maxSum = A.reduce((acc, curr) => acc + curr);
    let min = Infinity;
    while (minSum <= maxSum) {
        const minMaxSum = ~~((minSum + maxSum) / 2);
        const [k, possibleMin] = dividable(minMaxSum);
        if (k <= K) {
            min = Math.min(min, possibleMin);
            maxSum = minMaxSum - 1;
        } else
            minSum = minMaxSum + 1;
    }
    return min;
}

const r = solution(3, 5, [2, 1, 5, 1, 2, 2, 2])
console.log(r)