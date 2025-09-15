cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

#sort once - forever

cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print("\nHere is the sorted list in reverse alphabetical order:")
print(sorted(cars,reverse = True))

#sorted for temporary

cars.reverse()
print(cars)

#just reverse do not sort

print(cars)
print(len(cars))