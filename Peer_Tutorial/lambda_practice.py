"""
JSwart DAT129 Week 7
Peer tutorial Lambda functions explained. 
These are anonymous functions that can perform math functions as well as sorting.
"""

#funtion to perform an equation w/out using lamdas
def f(x):
	return 3*x+1

print("Equation without lambda equals", f(2))

#now, the same equation using lambda

g = lambda x: 3*x+1
print("Equation using lambda equals", g(2))

#using lambda to combine first and last names of users to a website
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print("Printing the 'full name' function using lambda:",full_name("     JASON", "swart"))

#using .sort and lambda to sort a list
HorrorAuthors = ["Stephen King", "Clark Ashton Smith", "Edgar Allen Poe", "H.P.Lovecraft", "Ramsey Campbell", "Brian Lumely", "Kim Newman", 
"Neil Gaiman", "Clive Barker"]

HorrorAuthors.sort(key = lambda name: name.split(" ")[-1].lower())
print("Printing the list of authors sorted alphabetically:", HorrorAuthors)

#Building a quadratic function using regular python functions followed by the same using lambda
def QuadraticFunc(a, b, c):
	"""This should return the function of f(x) = ax^2 + bx + c"""
	return lambda x: a*x**2 + b*x + c
f = QuadraticFunc(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))

#Running the same equation without giving the above function a name
print(QuadraticFunc(3, 0, 1)(2)) #3x^2+1 evaluated for x=2 should equal 13

#Using the built-in filter() function with lambda as a way to filter out elements in a sequence.
numList = [5,7,22,97, 54, 62, 77, 23, 73, 61]

newList = list(filter(lambda x: (x%2 != 0), numList))
print(newList)

#Lambdas also work with the built-in map() function. Using the above list with lambda and map() to create a new list that is doubled.
dubList = list(map(lambda x: x*2, numList))
print(dubList)

#The built-in reduce() function can be used with lambda to go over a list and create a sum of the whole.
#Please note that reduce needs to be imported from functools first.
from functools import reduce

sum = reduce((lambda x, y: x + y), numList)
print("The sum of the list called numList is:", sum)
