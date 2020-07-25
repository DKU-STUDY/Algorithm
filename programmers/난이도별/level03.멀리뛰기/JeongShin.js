function solution(n) {
    const result = {'1': 1, '2': 2}
    for (let i = 3; i <= n; i++) {
        result[i] = (result[i - 1] + result [i -2] ) %1234567
    }
    return result[n]
}

solution(4)