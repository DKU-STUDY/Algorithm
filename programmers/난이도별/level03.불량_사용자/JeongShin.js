function solution(user_id, banned_id) {
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

    console.log(matches);

    const fill = (stack, idx) => {
        if (idx === len) {
            console.log(stack);
            answer++;
            return;
        }
        matches[idx].forEach((str) => {
            if (stack.indexOf(str) === -1) {
                fill([...stack, str], idx + 1)
            }
        })
    };
    fill([], 0);
    console.log(answer);

}


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]);