const minDistance = function (word1, word2) {
    let dp = new Array(word1.length + 1).fill(null).map(() => (new Array(word2.length + 1).fill(0)));
    const [len2, len1] = [dp.length, dp[0].length];

    for (let i = 0; i < len2; i++)
        dp[i][0] = i;

    for (let i = 0; i < len1; i++)
        dp[0][i] = i;

    for (let i = 1; i < len2; i++)
        for (let j = 1; j < len1; j++)
            dp[i][j] = Math.min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (word1[i - 1] !== word2[j - 1]));

    return dp[len2 - 1][len1 - 1];
};