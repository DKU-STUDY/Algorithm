
/*
* 아직 풀고 있습니다 ㅠ ㅠ
* 어렵네요
* */

function solution(A) {
    const len = A.length;
    let fib = [1, 1];
    let idx = 2;
    while (fib[idx - 1] <= len) {
        const result = fib[idx - 1] + fib[idx - 2];
        fib.push(result);
        idx++;
    }
    fib = fib.reverse();
    const queue = [new frog(-1, 0)]
    const check = new Array(len + 1);
    while (queue.length) {
        const curr = queue.pop();
        for (const f of fib) {
            const next = pos + f;
            if (next === len)
                return count + 1;
            if (next < len && next >= 0) {
                if (A[next] === 1 && !check[next]) {
                    check[next] = true;
                    queue.push(new frog(next, count + 1))
                }
            }
        }
    }
    return -1;
}

class frog {
    constructor(pos, count) {
        this.pos = pos;
        this.count = count;
    }
}

const ans = solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0])

console.log(ans);
