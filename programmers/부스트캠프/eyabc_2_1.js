const keyboard = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '?']];

function solution (word) {
    let answer = '';

    const keyLen = keyboard.length;
    const wordArr = word.split('');
    let nowIdx = [0, 0];


    const inputIndex = wordArr.map(char => {
        for (let i = 0 ; i < keyLen ; i++) {
            const res = keyboard[i].indexOf(char);
            if (res !== -1)
                return [i, res];

            continue;
        }
    });

    const actionX = (diff) => diff < 0 ? '_' : '^';
    const actionY = (diff) => diff < 0 ? '>' : '<';

    inputIndex.forEach(idx => {
        const [diffX, diffY] = [
            nowIdx[0] - idx[0],
            nowIdx[1] - idx[1],
        ];

        answer = answer
            + actionX(diffX).repeat(Math.abs(diffX))
            + actionY(diffY).repeat(Math.abs(diffY))
            + '@';

        nowIdx = idx;
    });
    return answer;
}