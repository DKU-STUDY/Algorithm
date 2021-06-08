function solution(triangle) {
    let level = triangle.length - 1;
    if (level === 0)
        return triangle[0];
    const score = new Array(level + 1).fill(0);
    while (level > 0) {
        for (let i = 0; i < level; i++) {
            score[i] = Math.max(score[i] + triangle[level][i], score[i + 1] + triangle[level][i + 1])
        }
        level--;
    }
    return triangle[0] * 1 + score[0]
}

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]);
