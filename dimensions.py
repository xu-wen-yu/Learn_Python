dimentions = (200,50)
print(dimentions[0])
print(dimentions[1])

#dimentions[0] = 250失败

my_t = (3,)
#元组由逗号标识

for dimention in dimentions:
    print(dimention)

dimentions = (200,50)
print("Original dimentions:")
for dimention in dimentions:
    print(dimention)

dimentions = (400,100)
print("\nModified dimentions:")
for dimention in dimentions:
    print(dimention)