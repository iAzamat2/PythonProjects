fruits1 = ['apple', 'banana', 'orange', 'kiwi', 'pear']

fruits2 = ['banana', 'kiwi', 'tangerine']

result = []

for fruit in fruits1:
    if fruit in fruits2:
        result.append(fruit)

print(result)

result = [fruit for fruit in fruits1 if fruit in fruits2]

print(result)
