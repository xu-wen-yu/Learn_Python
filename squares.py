squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)#or squares.append(value**2)

print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)
print(sum(digits))
print(min(digits))
print(max(digits))

squares = [value**2 for value in range(1,11)]
print(squares)