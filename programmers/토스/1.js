/**
 * @param {string} name 마스킹할 이름
 * @returns {string} 마스킹된 이름
 */
function getMaskedName(name) {
    // 함수를 작성해주세요
    const len = name.length;
    const nameArr = new Array(len).fill('*');
    console.log({nameArr});

    nameArr[0] = name.charAt(0);
    nameArr[1] = name.charAt(1);

    console.log({nameArr});

    return nameArr.join('');
}
console.log(getMaskedName('제갈도건'));
