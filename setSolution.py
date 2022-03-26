first_set = {"dragon", "unicorn", "drake", "minotaur", "horse", "turtle"}
second_set = {"goose", "turtle", "chicken", "unicorn", "pig", "cow", "fox"}

intersection = set()
for member in first_set:
    if member in second_set:
        intersection.add(member)
        second_set.remove(member)

for member in intersection:
    if member in first_set:
        first_set.remove(member)


print(first_set)   #resulting in {"dragon", "drake", "minotaur", "horse"} in any order
print(second_set)   #resulting in {"goose", "chicken", "pig", "cow", "fox"} in any order