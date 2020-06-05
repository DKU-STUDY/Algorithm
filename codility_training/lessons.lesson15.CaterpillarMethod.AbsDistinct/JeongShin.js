function solution(A) {
    const set = new Set();
    A.forEach(el => {
        set.add(el < 0 ? el * -1 : el);
    })
    return set.size;
}

solution([-5, -3, -1, 0, 3, 6]);