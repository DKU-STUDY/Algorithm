/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
const longestCommonSubsequence = function (text1, text2) {
    const len1 = text1.length, len2 = text2.length;
    const dp = [];
    for (let i = 0; i <= len1; i++) {
        dp[i] = [];
        for (let j = 0; j <= len2; j++) {
            if (i === 0 || j === 0) {
                dp[i][j] = 0;
                continue;
            }
            if (text1[i - 1] === text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
                continue;
            }
            dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    return dp[len1][len2];
};

longestCommonSubsequence("abcde", "ace");
longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy");