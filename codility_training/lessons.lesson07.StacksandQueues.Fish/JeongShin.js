function solution(A, B) {
    const stack = [];
    let top = 0;
    A.forEach((fish, index) => {
        const direction = B[index] ? 1 : -1;
        if (top === 0 || direction === (top > 0 ? Math.sign(stack[top - 1]) : 0) || direction === 1)
            stack[top++] = fish * direction;
        else {
            while (top > 0 && Math.sign(stack[top - 1]) === 1) {
                top--;
                if (fish > stack[top])
                    stack[top] = fish * direction;
                else
                    break;
            }
            top++;
        }
    });
    // console.log(stack, top);
    return top;
}

solution([4, 3, 8, 1, 5], [0, 1, 1, 1, 0]);
