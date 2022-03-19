## Stack
___
A Python stack is a data structure that is based on the principle of last in first out (LIFO). In a stack when an item is added. It is only added to the end of the stack. As well as when you remove an item, is is only removed from the end.

### Push
This will add the item to the back of the stack array.
```sh
stack.append(value)
```
### Pop
Pop(value) will remove the last item of the stack array.
```sh
stack.pop()
```
### Size
SizeChecks for the size of the stack. When doing so you can compare stacks,
run loops with the size of the stack and check to see if the stack has a 
specific number of items in the array.
```sh
len(stack)
```
### Empty
Is important to check to see if a stack is empty and prevent an 
error of checking for a specific item if the stack is empty.
```sh
len(stack) == 0
```

### Top
Returns the reference to the top most item in the stack.
```sh
stack.top()
```

### Example
Create an empty stack.
```sh
stack = [] #resulting in [] 
```
Check to see if the stack is empty.
If it is empty then Push the value 5 to the end of the stack.
Else remove the last item from the stack with stack.pop().
```sh
if len(stack) == 0:
    stack.append(5)   # resulting in [5]
else:
    stack.pop()    # resulting in an error because the array is empty.
```

Push a new item to the back of the stack with stack.append(value).
```sh
stack.append(7)   # resulting in [5, 7]
```

We will push two #9s to the stack.
```sh
stack.append(9)   # resulting in [5, 7, 9]
stack.append(9)   # resulting in [5, 7, 9, 9]
```

Okay we really don't need two #9s so we can remove the last one by popping it
from the back of the array with stack.pop()
```sh
stack.pop()   # resulting in [5, 7, 9]
```
Size of the array len(stack).
```sh
print("This is the size of the stack: " + str(len(stack)))   # resulting in a print message of 3
```

Display all items in the stack.
```sh
print("This is all the items in the stack: " + str(stack))   # resulting in a print message of [5, 7, 9]
```

### Problem to solve
___
Write a program that will remove and add items to the stack to result
in the stack containing [9, 3, 6, 1, 8, 4, 4]
Use the starting code here
```sh
stack = [9, 3, 6, 9, 2, 1, 1]
```
You can check your code with the solution here: [Solution]
#### [Return to Welcome page]

[Solution]: <https://github.com/trevormw20/CSE-212-Final-Project/blob/master/stackSolution.py>
[Return to Welcome page]: <https://github.com/trevormw20/CSE-212-Final-Project/blob/master/Welcome.md>
