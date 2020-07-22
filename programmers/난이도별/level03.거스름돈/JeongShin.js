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

/*
* Dynamic Programming 을 통한 구현
* */

// function solution3(n, money) {
//     const table = {};
//     const len = money.length;
//     table.fill = (row, col, num) => {
//         table[row + ',' + col] = num;
//     };
//     table.get = (row, col) => {
//         return table[row + ',' + col];
//     };
//
//     // Initialize Table
//     for (let row = 0; row <= len; row++) {
//         table.fill(row, 0, 1);
//     }
//     for (let col = 1; col <= n; col++) {
//         table.fill(0, col, 0);
//     }
//
//     for (let row = 1; row <= len; row++) {
//         for (let col = 1; col <= n; col++) {
//             const [caseNotInclude, caseInclude] = [table.get(row - 1, col), table.get(row, col - money[row - 1])]
//                 .map(el => el === undefined ? 0 : el)
//             table.fill(row, col, caseInclude + caseNotInclude);
//         }
//     }
//     return table.get(len, n);
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