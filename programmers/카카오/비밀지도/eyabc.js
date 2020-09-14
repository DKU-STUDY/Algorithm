const convertToBinary = (num, n) => num.toString(2).padStart(n, '0');

function solution(n, arr1, arr2) {
    return arr1.map((num, i) => {
        const map1 = convertToBinary(num, n);
        const map2 = convertToBinary(arr2[i], n);

        let newMap = "";
        for (let i = 0; i < n ; i++) {
            newMap += ((map1[i]*1 + map2[i]*1) === 0) ? ' ' : '#';
        }
        return newMap;
    })
}

const assert = require('assert').strict;
require('./test.json').forEach(({ input, output }) => {
    assert.deepEqual(solution(...input), output);
});