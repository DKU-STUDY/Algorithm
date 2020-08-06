/**
 * @param {number} peopleCount 금액을 나눌 사람의 수
 * @param {number} amount 나눌 금액
 * @returns {number[]} 각자가 부담할 금액을 나타내는 숫자의 배열
 */
function splitDutchPayAmount(peopleCount, amount) {
    const div = ~~(amount / peopleCount);
    const remain = amount % peopleCount;
    const res = new Array(peopleCount).fill(div);
    res[0] += remain;
    return res;
}
console.log(
    splitDutchPayAmount(3, 4)
)