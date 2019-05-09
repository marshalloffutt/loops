# 4-13 Store 5 simple foods in a buffet tuple
buffet = ('meats', 'cheeses', 'breads', 'salads', 'desserts')

# use a for loop to print each food item
for food in buffet:
    print(food)

# try to modify one of them, and get error
# buffet[2] = 'cereals' 

# rewrite the tuple to change two items
# then print them using a for loop
buffet = ('meats', 'cereals', 'drinks', 'salads', 'desserts')

for food in buffet:
    print(food)
