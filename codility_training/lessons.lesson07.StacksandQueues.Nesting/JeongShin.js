function solution(S) {
    let top = 0;
    // forEach 문은 도중에 break로 loop 탈출이 불가능 하다 하여 일반 포문을 사용 하였습니다.
    for (const v of S) {
        if (top < 0)
            break;
        top += v === '(' ? 1 :  (v === ')') * -1
    }
    return !top*1;
}

solution(")(");
