function solution(s) {
    const map = s.replace(/([{}.,])/g, " ")
        .match(/\S+/g)
        .reduce((map, curr) => {
            curr *= 1;
            map.set(curr, (map.get(curr) || 0) + 1);
            return map
        }, new Map());
    return [...map]
        .sort((a, b) => b[1] - a[1])
        .map(v => v[0]);
}
