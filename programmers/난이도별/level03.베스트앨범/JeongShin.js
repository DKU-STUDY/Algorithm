function solution(genres, plays) {
    const [album, genre] = plays.reduce(([alb, gen], curr, idx) => {
        const genre = genres[idx];
        if (!alb[genre])
            alb[genre] = [];
        alb[genre].push([idx, curr]);
        gen[genre] = (gen[genre] || 0) + curr;
        return [alb, gen];
    }, [{}, {}]);

    const sortedGenre = [];

    for (const [key, val] of Object.entries(genre)) {
        sortedGenre.push([key, val]);
    }

    sortedGenre.sort((a, b) => b[1] - a[1]);

    return sortedGenre.reduce((answer, curr) => {
        const genre = curr[0];
        const sortedAlbum = album[genre];
        sortedAlbum.sort((a, b) => {
            if (a[1] === b[1]) // 앨범 판매량이 같을 경우 인덱스를 비교
                return b[0] - a[0];
            return a[1] - b[1]
        });
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