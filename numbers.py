# 4-3 Use a for loop to print numbers 1 to 20
twenty = list(range(1,21))
print(twenty)

## 4-4 Use a for loop to print numbers 1 to 1,000,000
one_million = list(range(1,1000001))
# print(one_million)

# 4-5 Print min, max, and sum from the one_million list
print(min(one_million))
print(max(one_million))
print(sum(one_million))

# 4-6 Make a list of odd numbers from 1-20
odds = list(range(1,21,2))
print(odds)

# 4-7 Make a list of multiples of 3 from 3 to 30
# use a for loop to print
threes = list(range(3,30,3))

for number in threes:
    print(number)

#4-8 & 4-9 Make a list of first 10 cubes, and prit using for loop
cubes = [value**3 for value in range(1,11)]

for cube in cubes:
    print(cube)