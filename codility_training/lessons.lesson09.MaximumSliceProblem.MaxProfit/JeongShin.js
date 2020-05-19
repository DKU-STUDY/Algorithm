function solution(A) {
    let [maxidx, minidx] = [0, 0];
    return A.reduceRight(([profit, max, min], curr, curridx) => {
        [max, maxidx] = curr > max ? [curr, curridx] : [max, maxidx];
        [min, minidx] = curr < min ? [curr, curridx] : [min, minidx];
        [min, minidx] = minidx > maxidx ? [curr, curridx] : [min, minidx];
        profit = maxidx > minidx ? Math.max(profit, max - min) : profit;
        return [profit, max, min];
    }, [0, 0, Infinity])[0];
}

let ans = solution([8, 9, 3, 6, 1, 2]);
console.log(ans);