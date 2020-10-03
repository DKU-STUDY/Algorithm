function solution(n) {
    let answer = [];
    let swap=0;

    answer.push(String(n));
    let h =answer[0].split('');     //숫자를 전부 한글자씩 배열에 분리
    const h_length = h.length;

    for(let i=0;i<h_length/2;i++)
    {       swap=h[i];
        h[i]=h[h.length-1-i];
        h[h.length-1-i]=swap;          //배열로 나열한 것을 뒤집어 나타내기
    }

    for(let i=0;i<h_length;i++)
        h[i]=Number(h[i]);      //뒤집어 나타내는것을 문자에서 숫자로 변환
    return h;
}
