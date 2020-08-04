/* 카드번호 유형인지 체크 */
const validForm = (arr) => arr.toString() === [4, 9, 14].toString() || arr.length === 0;
/* 카드번호가 16자리인지 체크 */
const validLength = (number) => number.length === 16;

const findHyphenIdx = () =>
    (arr, char, key) => {
        if (char === '-')
            arr.push(key);
        return arr;
    };

const processNumber = () =>
    ([odd, even, isEven], char) => {
        if (isEven) {
            let num = Number(char) * 2;
            if (num > 9)
                num = 1 + (num - 10);
            even += num;
        } else
            odd += Number(char);
        return [odd, even, !isEven];
    };

function solution (card_numbers) {
    const reduce = Array.prototype.reduce;

    return card_numbers.map(card => {
        const hyphenIdxArr = reduce.call(card, findHyphenIdx(), []);
        if (!validForm(hyphenIdxArr)) return 0;

        const number = card.replace(/\-/g, '');
        if (!validLength(number)) return 0;

        const [odd, even] = reduce.call(number, processNumber(), [0, 0, true]);
        return ((odd + even) % 10 === 0) * 1;
    });
}

console.log(solution(['3285-3764-9934-2453', '3285376499342453', '3285-3764-99342453', '328537649934245', '3285376499342459', '3285-3764-9934-2452'], [1, 1, 0, 0, 0, 0]));