/*
* stocksProfit = [ 6, 6, 3, 9 ,3, 5, 1 ], target = 12 과 같이 주어졌을때
* target, 12, 을 만드는 유니크한 pair 의 개수를 구하는 문제
* (6, 6), (3, 9) 2 개의 유니크한 페어가 존재 하므로 2를 반환
* */

function stockPairs(stocksProfit, target) {
    const pairs = {};
    const len = stocksProfit.length;
    stocksProfit.sort((a, b) => a - b);

    const checkDuplicate = (v1, v2) => {
        if (!pairs[v1 + ',' + v2] && !pairs[v2 + ',' + v1]) {
            pairs[v1 + ',' + v2] = true
        }
    };

    const binSearch = (tar, idx) => {
        let [low, high] = [0, len];
        while (low <= high) {
            const mid = ~~((low + high) / 2);
            if (stocksProfit[mid] === tar) {
                if (mid !== idx || (stocksProfit[mid - 1] === tar ||
                    stocksProfit[mid + 1] === tar)) {
                    checkDuplicate(stocksProfit[idx], tar)
                }
                break;
            } else if (stocksProfit[mid] < tar)
                low = mid + 1;
            else
                high = mid - 1;
        }
    };

    stocksProfit.forEach((val, idx) => {
        binSearch(target - val, idx);
    });
    return Object.keys(pairs).length
}