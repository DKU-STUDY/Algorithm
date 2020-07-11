function solution(budgets, M) {
    const dividable = (arr, bud) => 
        arr.reduce((acc, curr) => acc + Math.min(curr, bud), 0) <= M;

    const len = budgets.length;
    const sorted = budgets.sort((a, b) => a - b);
    let [low, high] = [sorted[0], sorted[len - 1]];

    if (M < low * len)
        return ~~(M/len);

    while (low <= high) {
        const mid = ~~((low + high) / 2);
        if (dividable(sorted, mid))
            low = mid + 1;
        else
            high = mid - 1;
    }

    return high;
}

solution([120, 110, 140, 150], 100);
