function solution(user_id, banned_id) {
    const cache = {'0': 1};
    const factorial = num => {
        let result;
        if (cache[num])
            result = cache[num];
        else
            result = cache[num] = num * factorial(num - 1);
        return result;
    };

    const rFact = Object.values(banned_id.reduce((acc, curr) => {
        acc[curr] = (acc[curr] || 0) + 1;
        return acc;
    }, {})).reduce((acc, curr) => acc * factorial(curr), 1);


    const matches = [];
    for (const s of banned_id) {
        const re = s.replace(/\*/g, "\\w") + '$';
        const match = (user_id.reduce((arr, str) => {
            const match = str.match(re);
            if (match) {
                arr.push(match.input);
            }
            return arr;
        }, []));
        matches.push(match);
    }

    const len = banned_id.length;
    let answer = 0;

    const combination = (stack, idx) => {
        if (idx === len) {
            answer++;
            return;
        }
        matches[idx].forEach((str) => {
            if (stack.indexOf(str) === -1) {
                combination([...stack, str], idx + 1)
            }
        })
    };

    combination([], 0);
    return answer / rFact;
}


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]);