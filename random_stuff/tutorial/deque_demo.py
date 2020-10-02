from collections import deque

my_stack = deque()

my_stack.append("k")
my_stack.append('c')
my_stack.append('a')
my_stack.append('t')
my_stack.append('s')
my_stack.reverse()

print(my_stack)
for i in range(len(my_stack)):
    print(my_stack.popleft())