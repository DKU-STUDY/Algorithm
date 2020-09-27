from sys import stdin


def z(size_of_mat, target):
    if size_of_mat == 2:
        # minimal case
        #print(f'minimal_case')
        if target == (0, 0):
            #print(0)
            return 0
        elif target == (1, 0):
            #print(1)
            return 1
        elif target == (0, 1):
            #print(2)
            return 2
        else:
            #print(3)
            return 3
    else:
        #print('recursion')
        mid_ind = (size_of_mat / 2 - 1, size_of_mat / 2 - 1)
        if target[0] <= mid_ind[0] and target[1] <= mid_ind[1]:
            new_size = int((size_of_mat / 2))
            #print(f'case01\nz({new_size}, {target})')
            return z(new_size, target)
        elif target[0] > mid_ind[0] and target[1] <= mid_ind[1]:
            new_size = int(size_of_mat / 2)
            new_target = int(target[0] - (size_of_mat / 2)), target[1]
            #print(f'case02\n{new_size ** 2} + z({new_size},{new_target})')
            return new_size ** 2 + z(new_size, new_target)
        elif target[0] <= mid_ind[0] and target[1] > mid_ind[1]:
            new_target = int(target[0]), int(target[1] - (size_of_mat / 2))
            new_size = int(size_of_mat / 2)
            return (new_size ** 2) * 2 + z(new_size, new_target)
        else:
            new_target = int(target[0] - (size_of_mat / 2)), int(target[1] - (size_of_mat / 2))
            new_size = int(size_of_mat / 2)
            return (new_size ** 2) * 3 + z(new_size, new_target)


size_of_mat, x, y = map(int, stdin.readline().split())

size_of_mat = 2 ** size_of_mat
#print(size_of_mat)

print(z(size_of_mat, (y, x)))
