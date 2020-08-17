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
    };
    dfs(0, 0);
    return answer
}

function solution2(numbers, target) {
    const len = numbers.length;
    let graph = [0];
    let lvl = 0;
    while (lvl < len) {
        const temp = [];
        graph.forEach((el) => {
            temp.push(el - numbers[lvl]);
            temp.push(el + numbers[lvl]);
        });
        graph = temp;
        lvl++
    }
    return graph.reduce((acc, curr) => acc + (curr === target), 0)
}

solution2([1, 1, 1, 1, 1], 3)