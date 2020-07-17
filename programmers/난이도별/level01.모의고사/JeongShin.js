/* 주석은 코드 리뷰 수정 */
function solution(answers) {
    // const students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    //     .map(arr => arr = {pattern: arr, len: arr.length})
    const students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
        .map(pattern => ({
            pattern,
            isMatch: (idx, ans) => (pattern[idx % pattern.length] === ans) * 1
        }))

    const scores = answers.reduce((scores, currAns, idx) => {
        return scores.map((currScore, currStudent) =>
            // { const {pattern, len} = students[currStudent];
            // return currScore + (pattern[idx % len] === currAns) }
            currScore + students[currStudent].isMatch(idx, currAns)
        )
    }, new Array(3).fill(0));

    const max = Math.max(...scores);

    return scores.reduce((arr, score, idx) => {
        score === max ? arr.push(idx + 1) : 0
        return arr;
    }, []).sort((a, b) => a - b);
}

function solution2(answers) {
    const students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
        .map(pattern => ({
            pattern,
            isMatch: (idx, ans) => (pattern[idx % pattern.length] === ans) * 1
        }));

    const scores = answers.reduce((scores, currAns, idx) => {
        return scores.map((currScore, currStudent) =>
            currScore + students[currStudent].isMatch(idx, currAns))
    }, new Array(3).fill(0));

    const max = Math.max(...scores);

    return scores.reduce((arr, score, idx) => {
        score === max ? arr.push(idx + 1) : 0;
        return arr;
    }, []).sort((a, b) => a - b);
}

solution([1, 2, 3, 4, 5])