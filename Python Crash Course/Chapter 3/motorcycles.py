# original code
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

# to add 1 more to the list we use append
#motorcycles.append('ducati')
#print(motorcycles)

#to start with empty list and then use append to add items to list
#motorcycles = []

#motorcycles.append('honda')
#motorcycles.append('yamaha')
#motorcycles.append('suzuki')

#print(motorcycles)

#inserting elements in a list by assigning postion
#motorcycles = ['honda', 'yamaha', 'suzuki']

#motorcycles.insert(0, 'ducati')
#print(motorcycles)

#Remove elements from the list, you can also remove a postion if you know it
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#del motorcycles[0]
#print(motorcycles)

#Removing an item using pop() method
# pretty much removes last item from list but you can still use it when
# assigned to another variable.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#Popping items from any position in a list

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

# Removing an Item by Value
# Only delted the first occurance of the value specified. If more, than use a loop.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)