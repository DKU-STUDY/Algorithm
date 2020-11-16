function solution(s) {
    let top = 0;
    for (const curr of s) {
        if (curr === "(")
            top++;
        if (curr === ")") {
            if (top === 0)
                return false;
            top--;
        }
    }
    return top === 0
}

solution("()()");