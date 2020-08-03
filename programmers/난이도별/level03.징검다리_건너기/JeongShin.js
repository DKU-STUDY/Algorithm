function solution(stones, k) {
    const len = stones.length;

    const checkPossible = n => {
        let distance = 0;
        for (let i = 0; i < len; i++) {
            distance = stones[i] >= n ? 0 : distance + 1;
            if (distance >= k)
                return false;
        }
        return true;
    };

    let [low, high] = [1, 200000000];
    let answer;

    while (low <= high) {
        const mid = ~~((low + high) / 2);
        const result = checkPossible(mid);
        if (result) {
            answer = mid;
            low = mid + 1;
            continue;
        }
        high = mid - 1;
    }

    return answer;
}

solution([0, 1, 0, 3, 0, 0, 3, 0, 0], 3);