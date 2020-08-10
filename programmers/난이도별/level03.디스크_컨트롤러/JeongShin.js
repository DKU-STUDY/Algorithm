function solution(jobs) {
    let currTime = 0
    const queue = [...jobs]
    const result = []
    let len = queue.length

    // 도착한 순서대로 정렬하고 같은 시간에 도착 했을시 빨리 끝나는 순서대로 정렬
    queue.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0])

    queue.pop = () => {
        /* 현재 시각내에 할 수 있는 job이 없다면 가장 빠른거 다시 수행 */
        if (currTime < queue[0][0])
            return queue.shift()

        /* 현재 시각내에 할 수 있는 job 중 가장 빨리 끝나는 job 을 linear search */
        let i = 0, minIdx = 0;
        while (i < queue.length && queue[i][0] <= currTime) {
            minIdx = queue[i][1] < queue[minIdx][1] ? i : minIdx
            i++
        }
        return queue.splice(minIdx, 1).pop();
    }

    while (queue.length) {
        const [arrTime, serTime] = queue.pop();
        currTime = Math.max(arrTime, currTime);
        result.push(serTime + currTime - arrTime);
        currTime+=serTime;
    }

    return Math.floor(result.reduce((acc, curr) => acc + curr, 0) / len)
}

console.log(solution([[0, 3], [1, 9], [2, 6]]))
