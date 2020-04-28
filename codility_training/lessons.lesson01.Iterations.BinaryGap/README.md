# Iterations.BinaryGap

## 출처

https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

## 문제 해결 방법

### 0. Binary 관련 Method를 이용한다.

#### javascript
``` ts
const N: number = 32
const b: string = N.toString(2)
```

#### java
``` java
String b = Integer.toBinaryString(n);
```

### 1. indexOf를 이용한다.

#### javascript
``` js
const b = '1000100100010000000001'
b.indexOf('1', 1) // output 4
b.indexOf('1', 5) // output 7
b.indexOf('1', 8) // output 11
b.indexOf('1', 12) // output 21
```

#### java
``` java
String b = "1000100100010000000001";
b.indexOf("1", 1); // output 4
b.indexOf("1", 5); // output 7
b.indexOf("1", 8); // output 11
b.indexOf("1", 12); // output 21
```

### 2. Math.max를 이용한다.
``` js
const max = Math.max(7 - 4, 11 - 7, 21 - 11)
return max
```

#### java
``` java
// 4 7 11 21 에 대해서
int max = 7 - 4; // output 3
max = Math.max(max, 11 - 7) // output 4
max = Math.max(max, 21 - 11) // output 10
return max 
```