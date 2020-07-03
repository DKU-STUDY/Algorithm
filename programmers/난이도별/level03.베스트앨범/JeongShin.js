function solution(genres, plays) {
    const [album, genre] = plays.reduce(([alb, gen], curr, idx) => {
        const genre = genres[idx];
        alb[genre] = alb[genre] || [];
        alb[genre].push([idx, curr]);
        gen[genre] = (gen[genre] || 0) + curr;
        return [alb, gen];
    }, [{}, {}]);

    const sortedGenre = [];

    sortedGenre.push(...Object.entries(genre));

    sortedGenre.sort((a, b) => b[1] - a[1]);

    return sortedGenre.reduce((answer, curr) => {
        const genre = curr[0];
        const sortedAlbum = album[genre];
        sortedAlbum.sort((a, b) => a[1] === b[1] ? b[0] - a[0] : a[1] - b[1]);
        let count = 0;
        while (sortedAlbum.length && count < 2) {
            const idx = sortedAlbum.pop()[0];
            answer.push(idx);
            count++;
        }
        return answer;
    }, [])
}

// 기대 값 : [4,1,3,0]

const r = solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 800, 800, 2500])
console.log(r);