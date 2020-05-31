function solution(A) {
    const len = A.length;
    let fib = [1, 1];
    let idx = 2;
    while (fib[idx - 1] <= len) {
        fib.push(fib[idx - 1] + fib[idx - 2]);
        idx++;
    }
    const stack = [new frog(-1, 0)];
    const count = [];    // 최소 점프수만 index 별로 저장하는 배열
    A[len] = 1;
    while (stack[0] !== undefined) {
        const { pos, count } = stack.pop();
        for (const jump of fib) {
            const next = pos + jump;
            if (A[next] === 1) {
                const next_count = count[next] || Infinity;
                if (next_count > (count + 1)) {
                    stack.push(new frog(next, count + 1));
                    count[next] = count + 1;
                }
            }
        }
    }
    return count[len] === undefined ? -1 : count[len];
}

class frog {
    constructor(pos, count) {
        this.pos = pos;
        this.count = count;
    }
}

solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
