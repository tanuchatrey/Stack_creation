stack = []

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        return stack.pop()


# Push elements
push(10)
push(20)
push(30)
push(40)

print("Stack:", stack)

# Pop an element
print("Popped element:", pop())

print("Stack after pop:", stack)
