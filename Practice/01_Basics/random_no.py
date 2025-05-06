import random as rd
from decimal import Decimal

li = ["Quine", "King", "Spread", "Aarav", "Diamond"]
rd.shuffle(li)             # Shuffle happens here
print(li)                  # Now print the shuffled list

print(rd.Random()) #random object btwn 0 and 1
print(rd.randint(1, 10)) #random int btwn 1 and 10 , 10 is inclusive
print(rd.random()) #random float btwn 0 and 1
print(rd.uniform(1, 10)) #random float btwn 1 and 10 , 10 is inclusive
print(rd.choice([1, 2, 3, 4, 5])) #random choice from the list
print(rd.sample([1, 2, 3, 4, 5], 3)) #random sample from the list of size 3
print(rd.seed(10)) #random seed


print(0.1+0.1+0.1-0.3) # why 0.1+0.1+0.1-0.3 = 5.551115123125783e-17
# because of floating point precision error
#solution
# use decimal module to avoid floating point precision error
print(Decimal(0.1)+Decimal(0.1)+Decimal(0.1)-Decimal(0.3)) # 0.0

#fractional no
from fractions import Fraction
print(Fraction(1, 3)) # 1/3
print(Fraction(1, 3) + Fraction(1, 3)) # 2/3

#set operations
print({1, 2, 3} | {3, 4, 5}) # union of two sets
print({1, 2, 3} & {3, 4, 5}) # intersection of two sets
print({1, 2, 3} - {3, 4, 5}) # difference of two sets
print({1, 2, 3} - {3, 1, 2}) # empty set 

print(type({})) # dict
print(type(set())) # set
print(type([])) # list
print(type(())) # tuple

print(type(True)) # bool
print(False is 0) # false
print(True + 9) # 10