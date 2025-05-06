#quadratic equation
import math
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))

d=b**2 - 4*a*c
if d>0:
    root1= (-b + math.sqrt(d)) / (2*a)
    root2= (-b - math.sqrt(d)) / (2*a)
    print(f"The roots are: {root1:.2f} and {root2:.2f}")
elif d==0:
    root= -b/(2*a)
    print(f"The root is: {root:.2f}")
else:
    real= -b/(2*a)
    imag= math.sqrt(abs(d))/(2*a)
    print(f"The roots are: {real:.2f}+{imag:.2f}j and {real:.2f}-{imag:.2f}j")
