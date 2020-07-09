function solution(N) {
    const bin = N.toString(2);
    let max = 0;
    let prev = 1;
    for (let i = 1; i < bin.length; i++ ) {

        if (bin[i] === '1') {
            const value = i - prev;
            if (value > 1 && value > max ) {
                max = i - prev;
            }
            prev = i;
        }
    }
    return max;
}

function solution2(N) {
    const bin = N.toString(2);
    let max = 0;
    let prev = 0;
    for (let i = 1; i < bin.length; i++ ) {
        if (bin[i] === '1') {
            const value = i - prev;
            if (value > max ) {
                max = i - prev - 1;
            }
            prev = i;
        }
    }
    return max;
}

console.log(solution2(328) === 2)

