from sys import stdin


class Que:
    def __init__(self):
        self.que_data = []

    def push(self, data_in):
        self.que_data.append(data_in)

    def pop(self):
        if self.empty():
            print(-1)
        else:
            temp = self.que_data[0]
            self.que_data = self.que_data[1:]
            print(temp)

    def size(self):
        print(len(self.que_data))

    def empty(self):
        return len(self.que_data) == 0

    def front(self):
        if self.empty():
            print(-1)
        else:
            print(self.que_data[0])

    def back(self):
        if self.empty():
            print(-1)
        else:
            print(self.que_data[-1])


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
    if input_commend[0] == 'front':
        stack.front()
    if input_commend[0] == 'back':
        stack.back()



N = int(stdin.readline())
commend_list = []

for _ in range(N):
    commend_list.append(stdin.readline().rstrip('\n'))

new_stack = Que()

for commend in commend_list:
    check_commend(new_stack, commend)
