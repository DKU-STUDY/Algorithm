class BST:
    def __init__(self, data):
        self.root = Node(data, parent=None)

    def __str__(self):
        return str(self.in_order_traver(self.root))

    def in_order_traver(self, node):
        if node.left_child is None:
            if node.right_child is None:
                return node.data
            else:
                return node.data, self.in_order_traver(node.right_child)
        else:
            if node.right_child is None:
                return self.in_order_traver(node.left_child), node.data
            else:
                return self.in_order_traver(node.left_child), node.data, self.in_order_traver(node.right_child)

    def is_in(self, data, node):
        if node.data == data:
            # print(f'data already in')
            return True, node
        else:
            if (data > node.data) and (node.right_child is not None):
                return self.is_in(data, node.right_child)
            if (data < node.data) and (node.left_child is not None):
                return self.is_in(data, node.left_child)
            # print(f'tree don`t have same data\n\n   return_node \n      type: {type(node)}\n        data: {node.data}')
            return False, node

    def add_new_node(self, data):
        bul, parent_node = self.is_in(data=data, node=self.root)
        if not bul:
            # print('insert new node')
            new_node = Node(data, parent=parent_node)
            if new_node.data < parent_node.data:
                parent_node.left_child = new_node
            else:
                parent_node.right_child = new_node

    def compute_number_of_sp(self, start_val, end_val):

        def find_start_node(start_val):
            node = self.root
            while not((start_val == node.data) or ((start_val < node.data) and (node.left_child is None))):
                #print(f'searching_node.data:{node.data}')
                if node.data > start_val:
                    node = node.left_child
                else:
                    if node.right_child is None:
                        return None
                    else:
                        node = node.right_child
            return node

        def find_end_node(end_val):
            node = self.root
            while not((end_val == node.data) or ((end_val > node.data) and (node.right_child is None))):
                if node.data < end_val:
                    node = node.right_child
                else:

        start_node = find_start_node(start_val)
        #print(f'start_node.data :{start_node.data}')
        return start_node


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return self.data


class CountSemiPrimes:
    def __init__(self, N, P, Q):
        self.spacesize = N
        self.P = P
        self.Q = Q
        self.PQ_len = len(P)
        self.semi_prime_tree = self.count_semi_prime()
        """
        print(
            f'class inited\n self.N:{self.spacesize}    self.P: {self.P}    self.Q: {self.Q}    self.PQ_len: {self.PQ_len}    self.semi_prime_tree: {self.semi_prime_tree}')
        """

    def count_prime(self):
        prime_list = [i for i in range(2, int(self.spacesize / 2) + 1)]
        idx = 0
        while idx <= len(prime_list) - 1:
            i = idx + 1
            while i <= len(prime_list) - 1:
                if prime_list[i] % prime_list[idx] == 0:
                    prime_list.pop(i)
                i += 1
            idx += 1
        return prime_list

    def count_semi_prime(self):
        prime_list = self.count_prime()
        length_of_prime_list = len(prime_list)
        root_data = prime_list[0] * prime_list[int(length_of_prime_list / 2)]
        # print(f'rood_data : {root_data}')
        semi_prime_tree = BST(data=root_data)
        for i in range(length_of_prime_list):
            j = i
            while prime_list[j] <= self.spacesize / prime_list[i]:
                if prime_list[i] * prime_list[j] <= self.spacesize:
                    semi_prime_tree.add_new_node(prime_list[i] * prime_list[j])
                j += 1
                if j > length_of_prime_list - 1:
                    break
        return semi_prime_tree

    def compute_return_list(self):
        return_list = []
        length_of_semi_prime_list = len(self.semi_prime_list)
        if length_of_semi_prime_list == 0:
            return [0]
        for idx in range(self.PQ_len):
            the_former = 0
            the_latter = length_of_semi_prime_list - 1
            while self.semi_prime_list[the_former] < self.P[idx] and the_former <= length_of_semi_prime_list - 1:
                the_former += 1
            while self.semi_prime_list[the_latter] > self.Q[idx] and the_latter >= 0:
                the_latter -= 1
            the_latter += 1
            return_list.append(the_latter - the_former)
        return return_list


def solution(N, P, Q):
    semiprime_prob = CountSemiPrimes(N, P, Q)
    print(semiprime_prob.semi_prime_tree.in_order_traver(semiprime_prob.semi_prime_tree.root))
    for idx in range(len(P)):
        print(f'start_val : {P[idx]}')
        print(f'start_node_data: {semiprime_prob.semi_prime_tree.compute_number_of_sp(P[idx], Q[idx]).data}')
    return 0
    # return semiprime_prob.compute_return_list()


print(solution(P=[1, 4, 16], Q=[26, 10, 20], N=26))
