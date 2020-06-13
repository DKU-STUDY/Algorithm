function solution(K, A) {
    return A.reduce(([count, acc], curr) => acc + curr >= K ? [count + 1, 0] : [count, acc + curr], [0, 0])[0]
}

solution(4, [1, 2, 3, 4, 1, 1, 3])