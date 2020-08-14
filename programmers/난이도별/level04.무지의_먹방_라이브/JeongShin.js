function solution(food_times, k) {
    let foods = [];
    const len = food_times.length;

    food_times.forEach((v, i) => foods.push({time: v, index: i}));
    foods.sort((a, b) => a.time - b.time);

    const getNextIdx = (i, prevMin, height) => {
        while ((foods[i].time - prevMin) === height) {
            i++;
            if (i === len)
                return -1;
        }
        return i;
    };

    let i = 0;
    let prevMin = 0;

    while (i < len) {
        const currMin = foods[i].time;
        const foodChunk = (currMin - prevMin) * (len - i);

        if ((k - foodChunk) < 0)
            break;
        k -= foodChunk;

        if ((i = getNextIdx(i, prevMin, currMin - prevMin)) < 0)
            return -1;

        prevMin = currMin;
    }

    foods = foods.splice(i);
    foods.sort((a,b)=> a.index - b.index);

    return foods[k % foods.length].index + 1;
}

console.log(solution([3, 5, 1, 6, 5, 4], 20));