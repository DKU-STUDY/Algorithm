function solution(arr) {
    arr.splice(arr.indexOf(Math.min.apply(null,arr)),1);    //가장 작은 값을 가진 위치에 있는 값을 없앤다.
    return (arr.length==0)?[-1]:arr;    // 없앤후 값이 아예없으면 [-1]리턴 그게아니라면 arr리턴
}
