function solution(arr)
{
    var answer = [];
    let next = 0;
    let present = 0;
    for(let i =0 ; i < arr.length; i++){
        present = arr[i]
        next = arr[i+1]
        if (present === next){
            continue;
        }
        answer.push(arr[i])
    }
    return answer;
}
// 1번에서 효율성 문제로 못 풀었습니다. 
// 근데 또 돌리니까 이번엔 되네요.. 뭐지.. 흠 
// 아래 한 줄 코드 보고 filter라는 함수로 원하는 원소만 뽑아서 배열로 만드는게 좋네요!!



// eyabc 님의 코드 
function solution(arr) {
  return arr.filter((num, i) => num !== arr[i + 1]);
}