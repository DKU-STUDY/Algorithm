/*
* 첫 번째 시도 : recursive 하게 k 번째 경우의 수를 찾는 경우의 수 알고리즘
* 효율성에서 불합격 👉 k 번째 경우의 수까지 전에 존재하는 모든 경우의 수를 찾기 때문
* */

function solution(n, k) {
    const target = new Array(n).fill(null).map((el, idx) => idx + 1)
    let done = false;
    let answer = [];
    let trail = 0;
    const fill = arr => {
        const len = arr.length;
        if (done)
            return;
        if (len === n) {
            trail++;
            if (trail === k) {
                done = true;
                answer = [...arr];
            }
            return;
        }
        target.forEach((el) => {
            if (!~arr.indexOf(el)) {
                fill([...arr, el])
            }
        })
    }
    fill([])
    return answer;
}

// 몫과 나머지를 이용하여 n번의 반복문으로 k 번째 수를 찾는 알고리즘 구현
// 정확도 성능 둘다 합격

function solution2(n, k) {
    const arr = new Array(n).fill(null).map((el, idx) => idx + 1)
    const answer = []
    const cache = {'0': 1}
    const factorial = num => {
        let result
        if (cache[num])
            result = cache[num]
        else
            result = cache[num] = num * factorial(num - 1)
        return result
    }
    k--;
    let len;
    while ((len = answer.length) < n) {
        const divide = factorial(n - len - 1)
        const [quotient, remainder] = [k / divide, k % divide]
        const val = arr.splice(quotient, 1)[0];
        answer.push(val);
        k = remainder;
    }
    return answer
}

solution(4, 7)