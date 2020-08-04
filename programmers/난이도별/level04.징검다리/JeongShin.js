function solution(distance, rocks, n) {
    rocks.push(distance);
    rocks.sort((a, b) => a - b);

    const isPossible = (min) => {
        let [removed, prev] = [0, 0];
        for (const curr of rocks) {
            const currDistance = curr - prev;
            removed += currDistance < min;
            prev = currDistance < min ? prev : curr;
            if (removed > n)
                return false;
        }
        return true;
    };

    const binSearch = () => {
        let [left, mid, right] = [1, undefined, distance];
        let answer;
        while (left <= right) {
            mid = ~~((left + right) / 2);
            const result = isPossible(mid);
            if (result) {
                answer = mid;
                left = mid + 1;
                continue;
            }
            right = mid - 1;
        }
        return answer;
    };

    return binSearch();
}

solution(25, [2, 14, 11, 21, 17], 2)