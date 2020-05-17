function solution(A) {
    function solution(A) {
        // 배열 내에서 최소값을 빼고 나머지 합을 구함
        const func = arr => {
            return arr.reduce(([acc, min], val) => {
                return [acc + val, Math.min(val, min)]
            }, [0, Infinity]).reduce((acc, val) => acc - val)
        };
        // 음수 값중 다음에 오는 값이 양수인 인덱스는 x,z에 대한 후보가 됩니다.
        const candidate = A.reduce((arr, val, idx) => {
            val <= 0 && (A[idx + 1] > 0 || A[idx - 1] > 0) ? arr.push(idx) : null;
            return arr;
        }, []);

        if (candidate.length === 0)
            return func(A.splice(1, A.length - 2));

        candidate.unshift(0);
        candidate.push(A.length - 1);
        const candidateLen = candidate.length;
        let max = 0;
        candidate.forEach((start, start_index) => {
            while (start_index < candidateLen) {
                max = Math.max(max, func(A.slice(start + 1, candidate[++start_index] - 1)))
            }
        });
        return max;
    }
}

solution([3, 2, 6, -1, -1, 4, 5, -1, 3]);