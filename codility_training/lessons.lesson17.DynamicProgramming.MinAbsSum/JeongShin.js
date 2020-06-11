/*
아직 시간복잡도 측면을 해결하지 못했습니다.
* */
function solution(A) {
    const len = A.length;
    A.sort((a, b) => Math.abs(b) - Math.abs(a))
    if (len < 2)
        return Math.abs(A[len - 1] || 0);
    let set = new Set().add(0);
    A.forEach((x, idx) => {
        const next = new Set();
        for (const y of set) {
            const left = len - idx;
            if (y < left * Math.abs(x))
                next.add(Math.abs(x + y));
            next.add(Math.abs(x - y));
        }
        set = next;
    });
    return Math.min(...set)
}

solution([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3])
