function solution(routes) {
    let min = -Infinity;
    return routes.sort((a, b) => a[1] - b[1]).reduce((ans, [start, end]) => {
        if (min < start) {
            min = end;
            ans++;
        }
        return ans;
    }, 0);
}

solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]);
