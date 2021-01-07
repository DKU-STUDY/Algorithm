/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
const coinChange = function (coins, amount) {
    const len = coins.length;
    const dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    coins.sort((a, b) => a - b);
    for (let i = 0; i < len; i++) {
        const coin = coins[i];
        for (let j = 1; j <= amount; j++) {
            const prev = (dp[j - coin] + 1) || Infinity;
            dp[j] = Math.min(prev, dp[j]);
        }
    }
    return dp[amount] === Infinity ? -1 : dp[amount];
};

coinChange([1, 2, 5], 11);