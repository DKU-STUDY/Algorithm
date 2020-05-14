function solution(H) {
    const len = H.length;
    const stack = [];
    let count = 0;
    let top = 0;
    for (let i = 0; i < len; i++) {
        const curr = H[i];
        while (top > 0 && stack[top - 1] > curr) {
            top--;
        }
        if (top === 0 || stack[top - 1] < curr) {
            stack[top++] = curr;
            count++;
        }
    }
    return count;
}
