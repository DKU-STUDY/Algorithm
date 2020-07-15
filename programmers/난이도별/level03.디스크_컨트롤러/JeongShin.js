// function solution(jobs) {
//     const result = []
//     const len = jobs.length
//
//     let currTime = 0
//
//     const pop = arr => {
//         const idx = arr.findIndex((el) => el[0] <= currTime)
//         return arr.splice(idx, 1).pop()
//     }
//
//     jobs.sort((a, b) => {
//         const [a_arrive, a_service] = a;
//         const [b_arrive, b_service] = b;
//         return (a_service - a_arrive) - (b_service - b_arrive)
//     })
//
//     while (jobs.length) {
//         const [arr, ser] = pop(jobs)
//         currTime = Math.max(arr, currTime)
//         result.push(currTime - arr + ser)
//         currTime += ser
//     }
//
//
//     return Math.floor(result.reduce((acc, curr) => acc + curr, 0) / len)
// }
//
