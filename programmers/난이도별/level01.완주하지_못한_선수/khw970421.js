function solution(participant, completion) {
    let p;
    completion.forEach(function k(e){
        participant.splice(participant.indexOf(e),1);       // participant중에 completion이랑 포함되는애 제거
    })
    return participant.join();       //그중 남은거 return
}
console.log(
    solution(['leo', 'kiki', 'eden'], ['eden', 'kiki'] ) == 'leo',
    solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola'] ) == 'vinko',
    solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']) == 'mislav'
)
// 효율성 문제 발생


function solution(participant, completion)
{
    const participant_length=participant.length;

    participant.sort();
    completion.sort();

    for(let i=0;i<participant_length;i++)
        if(participant[i]!=completion[i])       // 정렬후에 같은위치에 다른 값이라면 그값은 완주하지 못한 값
            return participant[i];          // 완주하지 못한 참가자 return
}

// 효율성 문제 해결 ( 정렬 후 return 처리)
