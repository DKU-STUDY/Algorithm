function solution(n, lost, reserve) {
    let rest = n-lost.length;       //rest는 처음 인원에서 잃어버리지 않은 인원들
    let new_lost=[];

    for(let i=0;i<lost.length;i++){
        if(-1!=reserve.indexOf(lost[i]))        //lost에서의 값이 reserve에서도 있을때(여벌 체육복을 가져온 학생이 체육복을 도난당했을때)
        {
            rest++;                //자기 여벌로 자신의 옷 채우기
            reserve.splice(reserve.indexOf(lost[i]),1);   //그때의 reserve 값 제거
        }
        else
            new_lost.push(lost[i]);      //lost에서의 값이 reserve에서도 없을때(여벌 체육복을 가져오지않은 학생이 체육복을 도난당했을때)
    }

    for(let i=0;i<new_lost.length;i++){
        if(-1!=reserve.indexOf(new_lost[i]-1))        //자기보다 앞에있는 사람이 여벌이있을때
        {
            rest++;                 //여벌로 자신의 옷 채우므로 +1
            reserve.splice(reserve.indexOf(new_lost[i]-1),1); //그때의 여벌을 썼으므로 없애기
            continue;
        }
        if(-1!=reserve.indexOf(new_lost[i]+1))        //아니면 자기보다 뒤에있는 사람이 여벌이있을때
        {
            rest++;
            reserve.splice(reserve.indexOf(new_lost[i]+1),1);   //그때의 여벌을 썼으므로 없애기
            continue;
        }
    }
    return rest;    //최종 rest return
}

/* 정확도 효율성 문제 x
 (여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며,
 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.)
 이 부분에서 계속 문제가 생기고 오류가 나서 처음 여벌이있는 학생이 자신의 체육복을 도난당한경우를 나눠서 수행하니 문제해결

 */
