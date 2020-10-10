

function solution(n) {
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    for (let i = 1; i <= n; i++)
        for (let j = 1; j <= i; j++)
            // F (i, n) = G (i-1) * G (n-i)
            dp[i] += dp[j - 1] * dp[i - j];

    return dp[n];
}

solution(3);
