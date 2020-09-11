const JSTestModule = require('/Users/ey/DKU/Algorithm/JSTestModule.js');
const englishToNumber = {
    'S': 1,
    'D': 2,
    'T': 3,
};

function solution (dartResult) {
    const answer = [0, 0, 0];
    const dartLen = dartResult.length;
    const ansLen = answer.length;

    let i = 0, a = -1;
    while (a < ansLen && i < dartLen) {
        const currChar = dartResult.charAt(i);
        if (currChar === '#') {
            answer[a] *= -1;
            i++;
            continue;
        }
        if (currChar === '*') {
            answer[a] *= 2;
            answer[a - 1] && (answer[a - 1] *= 2);
            i++;
            continue;
        }
        if (dartResult.charAt(i + 1)) {
            let nextChar = dartResult.charAt(i + 1);
            const Squared = englishToNumber[nextChar];
            a++;
            if (!Squared) {
                answer[a] = (currChar + nextChar) ** englishToNumber[dartResult.charAt(i + 2)];
                i += 3;
               continue;
            }
            answer[a] = currChar ** Squared;
            i += 2;
        }
    }
    return answer.reduce((sum, value) => {
        sum += value;
        return sum;
    }, 0);
};

JSTestModule('/Users/ey/DKU/Algorithm/programmers/카카오/다트게임/test.json', solution);
