function solution(N) {
    const arr = new Array(2).fill(1);
    for (let i = 2; i <= N; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
    }
    return (arr[N] + (arr[N - 1] || 0)) * 2;
}
