// 이렇게 풀이 하니까 5개의 테스트에서 통과를 못하고 거의 다 0으로 나오는데 이유를 정확히 모르겠습니다
// mod 연산하면서 overflow가 발생해서 그런줄 알았는데 JS number 최대 값이 생각보다 많이 크던데 이유를 잘 모르겠습니다

// function solution(A, B) {
//     const max = Math.max(...A)
//     const fib = [];
//     [fib[0], fib[1]] = [0, 1];
//     for (let i = 2; i < max + 2; i++) {
//         fib[i] = fib[i - 1] + fib[i - 2];
//     }
//     return A.map((el, idx) => {
//         return fib[el + 1] & ((1 << B[idx]) - 1)
//     })
// }


function solution(A, B) {
    const [max_a, max_b] = [Math.max(...A), Math.max(...B)]
    const fibonacci = n => {
        const fib = [];
        [fib[0], fib[1]] = [0, 1];
        for (let i = 2; i < n + 2; i++)
            fib[i] = (fib[i - 1] + fib[i - 2]) & ((1 << max_b) - 1) // 이 부분에서 젤 큰 값으로 나누어 배열에 저장하면 에러 없이 잘 수행 되었습니다.
        return fib
    }
    const fib = fibonacci(max_a);
    return A.map((el, idx) => fib[el + 1] & ((1 << B[idx]) - 1))
}
