/*
* 모든 경우의 수 중에서 sum 이 n 인걸 찾는 재귀 알고리즘
* 👉 시간초과
* */

// function solution2(n, money) {
//     const len = money.length;
//     money.sort((a, b) => b - a)
//     let count = 0;
//     const getSum = (sum, idx) => {
//         if (n <= sum) {
//             if (sum === n)
//                 count++;
//             return;
//         }
//         for (let i = idx; i < len; i++)
//             getSum(sum + money[i], i)
//     }
//
//     getSum(0, 0)
//     return count;
// }


function solution(n, money) {
    const table = [];
    const len = money.length
    for (let i = 0; i <= n; i++){
        table[i] = i % money[0] ? 0 : 1;
    }
    for (let i = 1; i < len; i++) {
        for (let j = money[i]; j <= n; j++) {
            table[j] += table[j - money [i]]
        }
    }
    return table[n] % 1000000007
}

solution(5, [1, 2, 5])