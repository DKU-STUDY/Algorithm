function solution(A) {
    const len = A.length;
    const pos = [], neg = [];
    if (len < 4)
        return A.reduce((acc, curr) => curr * acc, 1);
    const number = num => num !== undefined ? num : 1;
    for (const val of A)
        val >= 0 ? pos.push(val) : neg.push(val);
    pos.sort((a, b) => b - a);
    neg.sort((a, b) => a - b);
    const neg_len = neg.length;
    return pos.length === 0 ? neg[neg_len - 1] * neg[neg_len - 2] * neg[neg_len - 3] :
        Math.max(number(pos[0]) * number(pos[1]) * number(pos[2]), number(pos[0]) * number(neg[0]) * number(neg[1]),
    );
}

solution([-5, -6, -4, -7, -10]);
