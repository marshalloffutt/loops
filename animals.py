animals = ['bat', 'giraffe', 'snake']

for animal in animals:
    print(animal)

for animal in animals:
    print("A " + animal + " would make a great pet.")

print("Any of these animals would make a great pet.")

animals.append('elephant')
animals.append('mouse')
animals.append('tiger')
animals.append('spider')
animals.append('dog')
animals.append('kangaroo')


# 4-10 Slices
print("The first three items in the list are:")
print(animals[0:3])

print("The second three animals are:")
print(animals[3:6])

print("The final three animals are:")
print(animals[6:9])
