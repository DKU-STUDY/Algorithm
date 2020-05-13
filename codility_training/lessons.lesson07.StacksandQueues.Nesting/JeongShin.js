function solution(S) {
    const len = S.length;
    let top = 0;
    // forEach 문은 도중에 break로 loop 탈출이 불가능 하다 하여 일반 포문을 사용 하였습니다.
    for (const v of S) {
        if (top < 0)
            break;
        S[i] === '(' ? top++ : top = S[i] === ')' ? top - 1 : top;
    }
    return !top*1;
}

solution(")(");
