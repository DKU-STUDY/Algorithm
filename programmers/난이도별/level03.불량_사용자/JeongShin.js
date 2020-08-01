function solution(user_id, banned_id) {
    const possible_id = [];
    for (const s of banned_id) {
        const matched = (user_id.reduce((arr, str) => {
                const r = str.match('^' + s.replace(/\*/g, ".") + '$');
                if (r)
                    arr.push(r.input);
                return arr;
            }, [])
        );
        possible_id.push(matched);
    }

    const answer = new Set();
    const checkPossibleAnswer = (stack) => {
        stack.sort();
        const r = stack.join('');
        if (!answer.has(r))
            answer.add(r);
    };

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