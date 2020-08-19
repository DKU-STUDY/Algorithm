/*
* a = ['ab','cd','ef']
* b = ['af', 'ee', 'ef']
* 다음과 같이 배열이 있을때 각 인덱스 별로 a[i] 와 b[i] 에 substring 이 있는지 여부 검사.
* 'YES', 'NO', 'YES' 를 순서대로 출력해야함.
* */

function commonSubstring(a, b) {
    const len = a.length;
    for (let i = 0; i < len; i++) {
        const [A, B] = [new Set(a[i]), new Set(b[i])];
        let found = false
        for (const w of A) {
            if (B.has(w)) {
                found = true;
                console.log('YES');
                break
            }
        }
        if (!found)
            console.log('NO');
    }
}

