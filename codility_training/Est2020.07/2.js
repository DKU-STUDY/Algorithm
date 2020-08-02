function solution (scores, k) {
    const arr = [];
    const len = scores.length;
    if (scores.length === 1) return 0;

    /* 앞 스코어와의 점수 차를 나타내는 배열을 만든다. */
    for (let i = 1 ; i < len ; i++) {
        arr.push({
            k: i,
            v: scores[i] - scores[i - 1],
        });
    }

    const slicePoint = arr.sort((a, b) => b.v - a.v)    // 점수차가 큰 순서대로 정렬한다.
        .slice(0, k - 1)    // 점수차가 가장 큰 key 들을 나누는 지점으로 선택한다.
        .sort((a, b) => Number(a.k) - Number(b.k)); // key 를 기준으로 다시 정렬한다.
        console.log({slicePoint});

    let before = 0;
    let sum = 0;
    for (const v of slicePoint) {
        /* 반복1: mostBigKey 인 2 기준으로 앞의 그룹을 만든다. 그러면 0~1 인덱스가 되고, 이때 gap 은 2 이다. 그리고 다음 그룹의 시작 인덱스를 v.k 로 재 할당한다. */
        /* 반복2: mostBigKey 인 5 기준으로 앞의 그룹을 만든다. 그러면 2~4 인덱스가 되고, 이때 gap 은 3 이다. 그리고 다음 그룹의 시작 인덱스를 v.k 로 재 할당한다. */
        sum += scores[v.k - 1] - scores[before];
        before = v.k;
    }
    /* sum 은 (k - 1) 개 그룹의 gap 의 차이의 합이고, 뒤의 두 항은 마지막 그룹의 인덱스의 합이다. */
    return sum + scores[len - 1] - scores[before];
}

console.log(
    solution([1, 3, 7, 8, 10, 15], 3) === 5,
    // solution([1, 2, 12, 14, 15], 2) === 4,
);
/*
오름차순 scores
 k개의 조 최대한 점수가 비슷한 학생
 각 조에서 가장 점수가 높은 학생의 점수와 가장 점수가 낮은 학생의 점수의 차이를 구한 후, 차이의 합이 최소가 되도록
  조에 적어도 1명의 학생
  한 명이므로 차이가 0
  낮은 학생의 차이의 합
 */