function solution(clothes) {
    const count = {}

    for (const c of clothes)
        count[c[1]] = (count[c[1]] || 0) + 1

    return Object.values(count).reduce((acc, curr) => {
        return acc * (curr + 1)
    }, 1) - 1;
}

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])