# Stack implementation in Python

stack = []

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print("Stack:", stack)

# Pop operation
print("Popped element:", stack.pop())

print("Stack after pop:", stack)

# Peek operation
print("Top element:", stack[-1])

# Check if stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")
