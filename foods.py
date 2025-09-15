my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
#不能使用friend_foods = my_foods,这会指向同一个列表

my_foods.append('cannoil')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)