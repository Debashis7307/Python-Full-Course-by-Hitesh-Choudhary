no=2**1000
print(no) # infinity no handling capacity

repr('Aarav')
str('Aarav')
print('Aarav')
#difference between repr and str
#repr is used to get the string representation of an object 
#and it returns a string that represents the value of the object. It does not return any otherthing.
#str is used to get the string representation of an object and it returns a string that represents the value of the object. It does not return any otherthing.

print(1==2<3) #False
# both are same
print(1==2 and 2<3) #False 

import math
print(math.pi) #3.141592653589793
print(math.floor(math.pi)) #3
print(math.floor(-4.2)) #-5
print(math.trunc(-4.9)) #-4 towords zero

print((2+3j)*5) #complex no
print(type(2+3j)) #complex

print(0o20) #octal no
print(0b1010) #binary no
print(0xff) #hexadecimal no

print(hex(255))
print(oct(16))
print(bin(10))

#bitwise operators
print(0b1010 & 0b1100) #8 & -> how many bits are same in both the numbers
# 1010 & 1100 = 1000 = 8
print(0b1010 | 0b1100) #14 | -> how many bits are same in both the numbers
# 1010 | 1100 = 1110 = 14
print(0b1010 ^ 0b1100) #6 ^ -> how many bits are different in both the numbers
# 1010 ^ 1100 = 0110 = 6
print(~0b1010) #-11 # ~ -> 1's complement of the number
# 1010 = 0101 = 5
print(0b1010 << 2) #40 # << -> left shift operator
# 1010 << 2 = 101000 = 40
print(0b1010 >> 2) #2 # >> -> right shift operator
# 1010 >> 2 = 10 = 2

# Random Library
import random as rd
print(rd.Random()) #random object btwn 0 and 1
print(rd.randint(1, 10)) #random int btwn 1 and 10 , 10 is inclusive
print(rd.random()) #random float btwn 0 and 1
print(rd.uniform(1, 10)) #random float btwn 1 and 10 , 10 is inclusive
print(rd.choice([1, 2, 3, 4, 5])) #random choice from the list
print(rd.sample([1, 2, 3, 4, 5], 3)) #random sample from the list of size 3
print(rd.shuffle([1, 2, 3, 4, 5])) #random shuffle the list
print(rd.seed(10)) #random seed

