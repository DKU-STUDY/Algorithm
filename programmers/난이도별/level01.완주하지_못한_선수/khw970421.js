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
