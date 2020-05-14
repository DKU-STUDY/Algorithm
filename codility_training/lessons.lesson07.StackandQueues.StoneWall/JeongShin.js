function solution(H) {
    let top = 0;
    return H.reduce(([stack, count], curr) => {
        while (top > 0 && stack[top - 1] > curr) {
            top--;
        }
        if (top === 0 || stack[top - 1] < curr) {
            stack[top++] = curr;
            count++;
        }
        return [stack, count];
    }, [[], 0])[1];
}

solution([8, 8, 5, 7, 9, 8, 7, 4, 8]);
