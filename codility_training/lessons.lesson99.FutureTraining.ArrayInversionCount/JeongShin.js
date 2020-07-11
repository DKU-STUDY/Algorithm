/*
* Solution 2 : O (n log n) 👉 Time Complexity of Merge Sort
* 🌟 IDEA : number of inversion in merge()
* let i = index of left sub - array & j = index of right sub - array
* if a[i] > a[j], (mid - i) inversions
*
* 출처 : https://www.geeksforgeeks.org/counting-inversions/
*
* */

function solution(A) {
    const merge = (arr, left, mid, right) => {
        let [i, j, k] = [left, mid, left];
        let inv_count = 0;
        const temp = [];
        while ((i <= mid - 1) && (j <= right)) {
            if (arr[i] <= arr[j])
                temp[k++] = arr[i++];
            else {
                temp[k++] = arr[j++];
                inv_count = inv_count + (mid - i);
            }
        }
        while (i <= mid - 1)
            temp[k++] = arr[i++];
        while (j <= right)
            temp[k++] = arr[j++];
        for (let i = left; i <= right; i++)
            arr[i] = temp[i];
        return inv_count;
    }
    const mergeSort = (arr, left, right) => {
        let mid, inv_count = 0;
        if (right > left) {
            mid = ~~((right + left) / 2);

            inv_count = mergeSort(arr, left, mid);
            inv_count += mergeSort(arr, mid + 1, right);

            inv_count += merge(arr, left, mid + 1, right);
        }
        return inv_count > 1000000000 ? -1 : inv_count;
    }

    return mergeSort(A, 0, A.length - 1);
}

/*
* Solution 2 : O (n ^ 2) 👉 Bad Idea !
* */

// function solution(A) {
//     const len = A.length;
//     let count = 0;
//     for (let i = 0; i < len; i++) {
//         const curr = A[i];
//         for (let j = i + 1; j < len - 1; j++) {
//             const next = A[j];
//             if (i < j && curr > next)
//                 count++;
//         }
//     }
//     return count;
// }



