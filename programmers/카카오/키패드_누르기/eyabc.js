// 폰 배열을 dictionary 로 생성
const phoneObj = (() => {
    const phone = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#'],
    ];

    return phone.reduce((obj = {} , numbers, x) => {
        numbers.forEach((number, y) => obj[number] = [x, y]);
        return obj;
    }, {});
})();


// 'right' -> 'R', 'left' -> 'L 로 바꿔주는 함수
const handToShort = (hand) => hand === 'left' ? 'L' : 'R';

// 왼쪽키패드, 오른쪽키패드 인지 아니면 중간키패드인지 구분해주는 함수
const getHand = (number) => {
    if ([1, 4, 7].includes(number)) return 'L';
    if ([3, 6, 9].includes(number)) return 'R';
    return false;
};

// 중간 키패드일때, 중간키패드와 왼손 혹은 오른손 키패드와의 간격을 계산하는 함수
const distanceOf2Points = ([x1, y1], [x2, y2]) =>
    Math.abs(x1 - x2) + Math.abs(y1 - y2);

// 중간 키패드일 때, 왼손이 가까운지 오른손이 가까운지 구한다.
const getCloseHand = (number, leftCurr, rightCurr, hand) => {
    // 중간키패드, 좌 우 키패드의 location 배열을 가져온다.
    const numberLocation = phoneObj[number];
    const leftLocation = phoneObj[leftCurr];
    const rightLocation = phoneObj[rightCurr];

    // 중간키패드 - 좌 키패드, 중간키패드 - 우 키패드 각각 얼마나 떨어져있는지 구한다.
    const diffFromLeft = distanceOf2Points(numberLocation, leftLocation);
    const diffFromRight = distanceOf2Points(numberLocation, rightLocation);


    const diff = diffFromLeft - diffFromRight;
    // 차이가 같을떄는 거리가 같으므로, hand (R, L) 를 리턴하고, 좌키패드가 더 멀면 오른손을, 우키패드가 더 멀면 왼손을 리턴한다.
    return (diff === 0) ? hand :
        (diff > 0) ? 'R' : 'L';
};

function solution (numbers, hand) {
    // 손의 움직임을 저장하는 변수
    let leftCurr = '*';
    let rightCurr = '#';

    // hand 를 움직인다.
    const changeLocation = (H, number) => {
        if (H === 'L') leftCurr = number;
        if (H === 'R') rightCurr = number;
    };

    // hand 인자를 'R', 'L' 으로 바꿔준다.
    const shortHand = handToShort(hand);

    // 각 숫자를 누른키가 어떤 손인지 반환하는 map 메서드
    return numbers.map(number => {
        // 키패드를 왼손으로 누를수 있는지 오른손으로 누를 수 있는지 혹은 중간키패드여서 계산이 필요한지 리턴하는함수.
        let result = getHand(number);
        // 중간 키패드여서 왼손인지 오른손으로 눌러야 하는지 결정해야 함수를 부른다.
        if (!result)
            result = getCloseHand(number, leftCurr, rightCurr, shortHand);

        // 키보드를 눌러 현재 손의 위치를 변경한다.

        changeLocation(result, number);

        // 'R' 혹은 'L' 를 리턴한다.
        return result;
    }).join(''); // 문자열로 만든다.
}

const assert = require('assert').strict;
require('./test.json').forEach(({ input, output }) => {
    assert.deepEqual(solution(...input), output);
});