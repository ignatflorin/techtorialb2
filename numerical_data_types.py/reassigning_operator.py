a = 7

print(a)

a = a + 10

print(a) # 17
print(type(a)) # integer
b = 4

b = a * b 
#What will be the result of print statement below ? 
print(b) # 68

a = a - b + b/4 + a * 3 - 7

print(a) # 10.0
print(type(a)) # the type of a will be float

num1 = 100

# add 50 to num1 

#num1 = num1 + 50 
# It will add 50 to num1 and reassign it to num1 again
num1 += 50
print(num1)

# It will divide num1 with 25 then it will reassign the result to num1
#num1 is 150
num1 /=25
num1 = int(num1)
print(num1) # 6

# num1 is 6
num1 *= 5
print(num1) # 30

# num1 is 30
num1 %=7
print(num1) #2

#num1 is 2
num1 **=4
print(num1)

















