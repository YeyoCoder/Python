""" 
Solve quadratic equation a**2x+bx+c=0
Case 1 - Repeated real roots 
  a=1, b=4, c=4
Case 2 - Different real roots
  a=1, b=-1, c=-6
Case 3 - Complex roots
  a=1, b=-2, c=2 
"""
print("Solve quadratic equation a**2x + bx + c = 0")

# Import complex math module
import cmath

#Input the coeficients
a=input("Input the coeficient a: ")
b=input("Input the coeficient b: ")
c=input("Input the  c: ")

# Convert input string to float
a=float(a)
b=float(b)
c=float(c)

# Calculate the discriminant
discriminant = (b**2)-(4*a*c)

# Find two solutions
sol1 = (-b-cmath.sqrt(discriminant))/(2*a)
sol2 = (-b+cmath.sqrt(discriminant))/(2*a)

# Print the solutions
print("The solutions are {0} and {1} ".format(sol1, sol2))
print("Finishing program...")

# Modified from https://www.programiz.com/