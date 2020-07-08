# 유클리드 알고리즘
두 양의 정수의 최대 공약수 (gcd)를 계산하는 문제를 해결합니다.

왜 이게 되는지 모르겠음.. 별로 알고싶지도 않아..!!

## 12.1 차를 이용한 유클리드 알고리즘
```javascript
function gcd (a, b) {
  if (a === b) return a;
  if (a > b) gcd(a - b, b);
  else gcd(a, b - a);
    
}
```

## 12.2 나누기를 이용한 유클리드 알고리즘
when, a > b
```javascript
function gcd(a, b) {
  if (a % b === 0) return b;
  else return gcd(b, a % b);
}
```

### 12.3 이진 유클리드 알고리즘
- shifting and parity testing
- divide and conquer technique

안됨
```javascript
function gcd(a, b, res) {
  if (a === b) return res * a;
  else if (a % 2 === 0 && b % 2 === 0) 
    return gcd( ~~(a / 2), ~~(b / 2), 2 * res) 
  else if (a % 2 === 0)
    return gcd(~~(a / 2), b, res)
  else if (b % 2 === 0)
    return gcd(a, ~~(b / 2), res)
  else if (a > b)
    return gcd(a - b, b, res)
  else 
    return gcd(a, b - a, res)
}
```

## Least common multiple
a*b / gcd(a, b)
