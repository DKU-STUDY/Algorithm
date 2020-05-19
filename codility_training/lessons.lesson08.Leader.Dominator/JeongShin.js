function solution(A) {
    const d = {};
    const goal = A.length / 2;
    for (const [idx, el] of A.entries()){
        d[el] = (d[el] || 0) + 1
        if (d[el]>goal)
            return idx;
    }
    return -1;
}
