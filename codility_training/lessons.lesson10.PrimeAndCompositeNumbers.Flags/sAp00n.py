#  [3, 2, 1]
#[0, 0, 0, 0, 0, 1, 0, 1, 0, 1]
#[1,5,3,4,3,4,1,2,3,4,6,2]
def solution(A):
    list_of_peaks = find_peaks(A)
    print(f'list_of_peaks= {list_of_peaks}')
    number_of_peaks = len(list_of_peaks)

    distance_of_peaks = []
    if number_of_peaks > 1:

        fst_peak = list_of_peaks[0]
        for peak_idx in list_of_peaks[1:]:
            currnet_peak = peak_idx
            distance_of_peaks.append(currnet_peak - fst_peak)
        print(f'distance_of_peaks= {distance_of_peaks}')

        max_num_of_flag = 1
        for i in range(len(distance_of_peaks) + 1, 1, -1):
            #print(f'i= {i}')
            temp = 1
            for j in range(len(distance_of_peaks)):
                if j == 0 and distance_of_peaks[j] >= i > temp:
                    temp += 1
                elif distance_of_peaks[j]-distance_of_peaks[j-1] >= i > temp:
                    temp += 1
            #print(f'temp= {temp}')
            max_num_of_flag = max(max_num_of_flag, temp)
        return max_num_of_flag

    else:
        return number_of_peaks


def find_peaks(A):
    list_of_peaks = []
    for idx in range(1,len(A)-1):
        #print(f'i: {idx}')
        past_elements = A[idx - 1]
        current_elements = A[idx]
        next_elements = A[idx + 1]

        if current_elements > past_elements and current_elements > next_elements:
            list_of_peaks.append(idx)
        #print(list_of_peaks)
    return list_of_peaks

A = [1,5,3,4,3,4,1,2,3,4,6,2]
print(solution(A))