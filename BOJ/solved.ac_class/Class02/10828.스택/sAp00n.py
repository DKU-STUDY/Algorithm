from sys import stdin


class Stack:
    def __init__(self):
        self.stack_data = []

    def push(self, data_in):
        self.stack_data.append(data_in)

    def pop(self):
        if self.empty():
            print(-1)
        else:
            temp = self.stack_data[-1]
            self.stack_data = self.stack_data[:-1]
            print(temp)

    def size(self):
        print(len(self.stack_data))

    def empty(self):
        if len(self.stack_data) == 0:
            return True
        else:
            return False

    def top(self):
        if self.empty():
            print(-1)
        else:
            print(self.stack_data[-1])


def check_commend(stack, str_line):
    input_commend = str_line.split()
    if input_commend[0] == 'push':
        stack.push(int(input_commend[-1]))
    if input_commend[0] == 'pop':
        stack.pop()
    if input_commend[0] == 'size':
        stack.size()
    if input_commend[0] == 'empty':
        if stack.empty():
            print(1)
        else:
            print(0)
    if input_commend[0] == 'top':
        stack.top()


N = int(stdin.readline())
commend_list = []

for _ in range(N):
    commend_list.append(stdin.readline().rstrip('\n'))

new_stack = Stack()

for commend in commend_list:
    check_commend(new_stack, commend)
