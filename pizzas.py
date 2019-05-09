pizzas = ['pepperoni', 'mushroom', 'cheese']

# use a for loop to print the name of each pizza
for pizza in pizzas:
    print(pizza)

# use a for loop to print a sentence using the name of each pizza
# and then add a closing line outside of the loop
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("I really like pizza.")

# 4-11
friend_pizzas = pizzas[:]

pizzas.append('pineapple')
friend_pizzas.append('anchovy')

print("\nThe favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)