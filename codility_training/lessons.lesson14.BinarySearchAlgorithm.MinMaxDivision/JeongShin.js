function solution(K, M, A) {
    const dividable = (sum) => {
        let max = 0;
        const k = A.reduce(([k, acc], curr) => {
            if (acc + curr > sum) {
                k++;
                acc = 0;
            }
            max = Math.max(acc + curr, max);
            return [k, acc + curr];
        }, [0, 0])[0]
        return [k + 1, max];
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