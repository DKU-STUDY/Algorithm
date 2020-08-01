// commaizeNumber 함수를 구현하세요.
// num은 Number 타입으로 들어온다고 가정합니다.
function commaizeNumber(num) {
    const numArr = (num + '').split('');
    const len = numArr.length;
    let newNumber = '';
    for (let i = len - 1 ; i > -1 ; i--) {
        newNumber =  numArr[i] + newNumber;
        if (i !== 0 && (len - i) % 3 === 0) newNumber =  ',' + newNumber;
    }
    return newNumber
}

console.log(commaizeNumber(1234567) === '1,234,567');
console.log(commaizeNumber(1) === '1');
console.log(commaizeNumber(12) === '12');
console.log(commaizeNumber(123) === '123');