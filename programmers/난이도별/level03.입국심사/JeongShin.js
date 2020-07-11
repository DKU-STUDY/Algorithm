function solution(n, times) {
    const count = t => {
        return times.reduce((acc, curr) => acc + Math.floor(t / curr), 0)
    };

    const len = times.length;

    let [low, high] = [Math.min(...times), Math.max(...times)].map((el => ((el * n) / len)));

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (count(mid) < n)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return low;
}
