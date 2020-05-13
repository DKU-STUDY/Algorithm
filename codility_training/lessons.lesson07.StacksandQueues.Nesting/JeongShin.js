function solution(S) {
    const len = S.length;
    const stack = [];
    let top = 0;
    // forEach 문은 도중에 break로 loop 탈출이 불가능 하다 하여 일반 포문을 사용 하였습니다.
    for (let i = 0; i < len; i++) {
        if (top < 0)
            break;
        S[i] === '(' ? stack[top++] = S[i] : top = S[i] === ')' ? top - 1 : top;
    }
    return !top*1;
}

solution(")(");
