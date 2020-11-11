const getCount = (N, stages) =>
    stages.reduce(([count, allSolved], number) => {
        if (number > N)
            allSolved += 1;
        else
            count[number - 1] += 1;
        return [count, allSolved];

    }, [new Array(N).fill(0), 0]);

const getPrefixSum = (count, allSolved) =>
    count.reduceRight((arr, value, key) => {
        let newVal = (key === (count.length - 1)) ?
            allSolved + (value || 0) :
            (value || 0) + (arr[arr.length - 1]);
        arr.push(newVal);
        return arr;
    }, []);

const getFailRate = (prefixSum, count) =>
    prefixSum.map(((solvedNumber, idx) => {
        const notSolvedNumber = count[count.length - 1 - idx] || 0;
        return {
            stage: count.length - idx,
            failRate: notSolvedNumber === 0 ? 0 : (notSolvedNumber / solvedNumber),
        };
    }));

const getSortedRate = (failRate) =>
    failRate.sort((a, b) => {
        const diff = b.failRate - a.failRate;
        if (diff === 0) return a.stage - b.stage;
        return diff;
    }).map(v => v.stage);

function solution (N, stages) {
    const [count, allSolved] = getCount(N, stages);
    const prefixSum = getPrefixSum(count, allSolved);
    const failRate = getFailRate(prefixSum, count);
    return getSortedRate(failRate);
}


const assert = require('assert').strict;
require('./test.json').forEach(({ input, output }) => {
    assert.deepEqual(solution(...input), output);
});
