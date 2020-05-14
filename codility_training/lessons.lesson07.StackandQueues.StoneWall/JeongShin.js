function solution(H) {
    return H.reduce(([stack, count, top], curr) => {
        while (top > 0 && stack[top - 1] > curr) {
            top--;
        }
        if (top === 0 || stack[top - 1] < curr) {
            stack[top++] = curr;
            count++;
        }
        return [stack, count, top];
    }, [[], 0, 0])[1];
}

solution([8, 8, 5, 7, 9, 8, 7, 4, 8]);
