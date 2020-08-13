from sys import stdin


class Deck:
    def __init__(self):
        self.deck_data = []

    def push_back(self, data_in):
        temp = data_in
        self.deck_data = [temp] + self.deck_data

    def push_front(self, data_in):
        self.deck_data.append(data_in)

    def pop_front(self):
        if self.empty():
            print(-1)
        else:
            temp = self.deck_data[-1]
            self.deck_data = self.deck_data[:-1]
            print(temp)

    def pop_back(self):
        if self.empty():
            print(-1)
        else:
            temp = self.deck_data[0]
            self.deck_data = self.deck_data[1:]
            print(temp)

    def size(self):
        print(len(self.deck_data))

    def empty(self):
        if len(self.deck_data) == 0:
            return True
        else:
            return False

    def front(self):
        if self.empty():
            print(-1)
        else:
            print(self.deck_data[-1])

    def back(self):
        if self.empty():
            print(-1)
        else:
            print(self.deck_data[0])


def check_commend(stack, str_line):
    input_commend = str_line.split()
    if input_commend[0] == 'push_front':
        stack.push_front(int(input_commend[-1]))
    if input_commend[0] == 'push_back':
        stack.push_back(int(input_commend[-1]))
    if input_commend[0] == 'pop_front':
        stack.pop_front()
    if input_commend[0] == 'pop_back':
        stack.pop_back()
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

new_stack = Deck()

for commend in commend_list:
    check_commend(new_stack, commend)
