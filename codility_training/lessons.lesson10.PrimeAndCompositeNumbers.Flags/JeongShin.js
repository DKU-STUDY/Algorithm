
/*
* 이 문제는 아직 풀고 있는중 입니다 ,,,
* */

function solution(A) {
    if (A.length < 3)
        return 0
    // return A.reduce(([flags, last_flag], curr, idx) => {
    //     const [p, n] = [A[idx - 1], A[idx + 1]] || curr
    //     if (curr > p && curr > n) {
    //         if ((last_flag === -1) || (last_flag + flags >= idx))
    //             return [flags + 1, idx]
    //     }
    //     return [flags, last_flag]
    // }, [1, -1])[0]
    const peeks = A.reduce(([stack, last_peek], curr, idx) => {
        const [p, n] = [A[idx - 1], A[idx + 1]] || curr
        if (curr > p && curr > n) {
            last_peek !== -1 ? stack.push(idx - last_peek) : null
            return [stack, idx];
        }
        return [stack, last_peek];
    }, [[], -1])[0];
    console.log(peeks)
}


console.log(solution([1, 5, 2]))