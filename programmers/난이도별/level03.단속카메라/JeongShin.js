function solution(routes) {
    let ans = 0;
    let min = -Infinity;
    routes.sort((a, b) => a[1] - b[1]);
    routes.forEach(val => {
        if (min < val[0]) {
            min = val[1];
            ans++;
        }
    })
    return ans;
}

solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]);
