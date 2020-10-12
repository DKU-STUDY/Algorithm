function solution(a, b) {
    const days=[31,29,31,30,31,30,31,31,30,31,30,31];
    const weeks = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
    let sum=0;
    for(let i=0;i<a-1;i++)
        sum+=days[i];       //전달 까지의 더함

    return weeks[(sum+b+4)%7]; //일수를 더하고 2015 12월31일 목요일 기준으로 4를 더한걸 합치고 7로 나누어 날짜찾기
}
