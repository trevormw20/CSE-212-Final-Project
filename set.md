## Set
___
An unordered array in which cannot have duplicates. Each item gets its own slot but cannot be reffered by index. Items cannot be changed as well. Sets can be very useful where unique values need to be assigned and not duplicated within an array.

<br>

### Add
Add a new item to the set if an item is not already in the set. 
```sh
this_set.add(value)
```
You can also perform a union between two sets with add to combine the two. No duplicates will be added.
```sh
first_set.add(second_set)
```

<br>

### Remove
Unlike pop in a stack will remove the last item in the array. Remove in a Set will remove the specific value from anywhere in the array.
```sh
this_set.remove(value)
```

<br>

### Member
Any member of a set can be located anywhere in the array by specifiying the item inside the set. This can be helpful for if statements, loops, and remove methods.
```sh
if value in this_set:
```

<br>

### Intersection
Show which members are located in both Sets being compared.
```sh
intersection = set()
for member in first_set:
    if member in second_set:
        intersection.add(member)

```

<br>

### Size
The size of a Set can be determined by using the len method. This can be helpful in loops and if statments. 
```sh
set_length = len(this_set)
```
For loops will automatically determine the size of a Set like this example. Printing out each item in the Set.
```sh
for x in this_set:
    print(x)
```

<br>

### Example
Create and fill a Set.
```sh
first_set = {"car", "truck", "motorcycle"}
```
Remove an item from the Set.
```sh
first_set.remove("motorcycle")

print(first_set)   #resulting in {"car", "truck"} in any order
```
Creat a new Set and fill it.
```sh
second_set = {"train", "bus", "taxi"}
```

Union both the first set and the second set together.
```sh
first_set.add(second_set)

print(first_set)   #resulting in {"car", "truck", "train", "bus", "taxi"} in any order

print(len(first_set))   #resulting in 5
```
Check to see if a member is located within the Set.
```sh
if "train" in first_set:
    print("Train is in the first_set.")   #resulting in Train is in the first_set.

if "motorcycle" in first_set:
    prting ("Motorcycle is in the first_set.")   #resulting in an error because motorcyle is not found in first_set
```

<br>

### Problem to solve
___
With the provided Sets. Write a program that removes all itersecting members in both Sets.
```sh
first_set = {"dragon", "unicorn", "drake", "minotaur", "horse", "turtle"}
second_set = {"goose", "turtle", "chicken", "unicorn", "pig", "cow", "fox"}



print(first_set)   #resulting in {"dragon", "drake", "minotaur", "horse"} in any order
print(second_set)   #resulting in {"goose", "chicken", "pig", "cow", "fox"} in any order
```

[Solution]: <https://github.com/trevormw20/CSE-212-Final-Project/blob/master/setSolution.py>
[Return to Welcome page]: <https://github.com/trevormw20/CSE-212-Final-Project/blob/master/Welcome.md>
