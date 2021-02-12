function solution(n, lost, reserve) {
    let answer = 0;
    let arr = [];
    lost.sort((a,b) => a-b);
    reserve.sort((a,b) => a-b);
    let lost_num = 0;
    for(let i =0; i < n; i++){
        if(lost[lost_num] === i+1){
            arr[i] = 0;
            lost_num++;
        }
        else{
            arr[i] = 1;
        }
    }
    for(let i =0; i<reserve.length; i++){
        if(arr[reserve[i] -1] === 0){
            arr[reserve[i] - 1] = 1;
            reserve[i] = 0;
        }
    }
    for(let i = 0; i < reserve.length; i++){
        if(reserve[i] === 0)
            continue;
        if(reserve[i] !== 1){
            if(arr[reserve[i] - 2] === 0){
                arr[reserve[i] - 2] = 1;
                continue;
            }
        }
        
        if(reserve[i] !== n){ 
            if(arr[reserve[i]] === 0){
                arr[reserve[i]] = 1;
            }
        }
    }
    return (arr.filter((i) => i >= 1)).length;
}

// 문제풀이:
// 우선 탐욕법이라는 알고리즘을 모르고 도전을 해봤다. (미루면 끝이 없을 것 같아서)
// 처음엔 왼쪽이나, 오른쪽이나 주기만 하면 된다고 생각해서 
// 왼쪽 사람부터 주고, 이미 있으면 오른쪽 사람을 주도록 코드를 짰다.
// 먼저 for문을 한번 돌면서 없는 사람은 0, 있는 사람은 1인 배열로 만들었다. (ex. [1,0,1,0,1])
// 그 후 여벌 옷을 가진 사람의 리스트인 reserve를 돌면서 
// 왼쪽사람(reserve[i] - 2), 오른쪽사람(reserve[i])의 값이 0인 사람은 1로 바꿔주게 했다.a


// 문제점 1
//  - 맨 왼쪽(1), 맨 오른쪽(n)은 각각 한쪽씩만 옷을 줄 수 있다
//  - 그래서 앞에 if문을 추가했다. 
//  - ex. reserve[i] !== 1 , reserve[i] !== n

// 문제점 2
//  - 잃어버린 사람의 배열과 여벌옷 가진 사람의 배열이 순서대로가 아닐 수 있다
//  - 따라서 하기 전에 먼저 두 배열을 숫자에 맞게 sort해줬다 

// 문제점 3
//  - 여벌옷을 가진 사람도 뺏길 수 있다는 걸 알게되었다. 
//  - 즉, reserve에도, lost에도 둘 다에 있는 번호가 존재할 수 있다.
//  - 이 경우 다른 사람에게 옷을 못 주고 자신이 입는다고 했다.
//  - 5 [2,3] [1,2] 4 이렇게 예시를 넣으면 알 수 있다
//  - 자기 자신에게 여벌옷을 주는 경우를 생각 못하면 이 경우에서 답이 5가 나온다. 
//  - (1이 2를 주고, 2가 3을 주게 되어서, 사실 2는 자신에게 주고 1이 3을 줄 수 없는 경우가 된다) 

// 문제점 4
//  - 그걸 같은 for문에서 돌릴려고 하니까 문제가 되어서
//  - 따로 for문을 돌려 여벌옷 있는 자기 자신이 0이면 자기 자신을 1로 만들고
//  - 사용한 여벌옷 값을 0으로 바꿔준다. 
//  - 이 후 밑에 for문에서는 0이면 이미 자기 자신에게 사용한 사람이니 넘어간다. 


// 다른 사람 코드 리뷰(junilhwang.js)
// const arr = [-1]
// for (let i = 1; i <= n; i++) arr[i] = 1
// lost.forEach(v => arr[v] -= 1)
// reserve.forEach(v => arr[v] += 1)
// for (let i = 1; i <= n; i++) {
//   if (arr[i] === 2 && arr[i - 1] === 0) arr[i - 1] = arr[i] = 1
//   if (arr[i] === 2 && arr[i + 1] === 0) arr[i + 1] = arr[i] = 1
// }
// return arr.filter(v => v >= 1).length;

// 먼저 n까지 모두 1로 만들고, lost에 해당되는 index의 값을 0으로 바꿔준다
// 그리고 reserve에 해당되는 index의 값에 1을 더해준다.
// 이로써 0,1,2 값을 가진 배열이 생긴다. (0은 없는 사람, 1은 있는 사람, 2는 여벌옷 있는 사람)
// 이러면 위에서 자기자신에게 주는 사람의 케이스를 생각 안해도 된다! 굿 

// 다음 마지막으로 for문을 돌리면서 2인 사람만 왼쪽 혹은 오른쪽에게 값을 나눠준다. 
// 그리고 맨 마지막 filter를 통해 1보다 큰 값을 가진 요소만 뽑아 길이를 return 한다. 


// 배운점:
// 탐욕법, 처음 해보는 풀이었다. 
// 여러 조건을 주고 최적화, 최적의 방법을 찾는 것이 탐욕법이다. 
// 좀 더 공부할 필요성을 느꼈고, 조건대로 해보는 것이 좋다는 생각이 들었다. 
