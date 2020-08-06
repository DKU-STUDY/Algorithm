function solution(user_id, banned_id) {
    const possible_id = [];
    for (const s of banned_id) {
        const regEx = '^' + s.replace(/\*/g, ".") + '$';
        possible_id.push(user_id.reduce((arr, str) => {
                const r = str.match(regEx);
                if (r)
                    arr.push(r.input);
                return arr;
            }, [])
        );
    }

    const answer = new Set();
    const checkPossibleAnswer = (stack) => answer.add(stack.sort().join(''));

    const len = banned_id.length;

    const combination = (stack, idx) => {
        if (idx === len) {
            checkPossibleAnswer(stack);
            return;
        }
        possible_id[idx].forEach((str) => {
            if (!~stack.indexOf(str)) {
                combination([...stack, str], idx + 1);
            }
        })
    }

    combination([], 0);

    return answer.size;
}


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]);