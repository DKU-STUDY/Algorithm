function solution(numbers, target) {
    const len = numbers.length;
    let answer = 0;
    const dfs = (sum, idx) => {
        if (idx === len) {
            answer += (sum === target)
            return;
        }
        dfs(sum + numbers[idx], idx + 1)
        dfs(sum - numbers[idx], idx + 1)
    }
    dfs(0, 0)
    return answer
}

function solution2(numbers, target) {
    const len = numbers.length;
    let graph = [0];
    let lvl = 0;
    while (lvl < len) {
        const temp = [];
        graph.forEach((el) => {
            // spread operator 를 사용해서 temp 를 매번 재 할당해주니 객체가 복사되는 시간 때문에
            // 시간초과로 인해 push 메서드를 사용 하였습니다.
            // temp = [...temp, el - numbers[lvl], el + numbers[lvl]]
            temp.push(el - numbers[lvl]);
            temp.push(el + numbers[lvl]);
        })
        graph = temp;
        lvl++
    }
    return graph.reduce((acc, curr) => acc + (curr === target), 0)
}

solution2([1, 1, 1, 1, 1], 3)
