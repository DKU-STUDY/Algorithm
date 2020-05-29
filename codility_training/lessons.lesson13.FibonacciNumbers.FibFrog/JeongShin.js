function memoize(fn) {
    const cache = {};
    return function (...args) {
        if (cache[args])
            return cache[args]
        const result = fn.apply(this, args);
        cache[args] = result;
        return result
    }
}

function fib(n) {
    if (n < 2) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

fib = memoize(fib);

function solution(A) {
    const len = A.length;
    const fibs = {};
    let result = 0, i = 0
    while (result < len) {
        result = fib(i++)
        fibs[result] = true;
    }
    // 가장 첫 점프를 할 가장 큰 피보나치 수 index를 찾음
    let curr = -1;
    A.forEach((val, idx) => {
        if (val === 1 && fibs[idx + 1] === true)
            curr = idx;
    })
    if (curr === -1)
        return 0;

    while (curr < len) {
        let next = undefined;
        for (let idx = curr + 1; idx < len; idx++) {
            if (A[idx] === 1 && A[idx - curr] === true)
                next = curr;
        }
        console.log(curr);

        if (next === undefined)
            break;
        curr = next;
    }

}

solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0])