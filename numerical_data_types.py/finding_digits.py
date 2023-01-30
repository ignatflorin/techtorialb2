
a=123
# the number a can be any digit number
#solution should work for every number
#find the multiplication of digits of number a
# when integre divide number with 10 it will get rid of the last digit of the number
# when i find remiunder with 10 i will get the last digit of the number

last_digit = a % 10
first_two_digits = a // 10
middle_digit = first_two_digits % 10
first_digit = first_two_digits // 10
print("multiplications of eachdigit of number a is",first_digit*last_digit*middle_digit)






















