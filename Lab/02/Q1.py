def trapezoid(a, b, h):
    return ((a+b)/2)*h


def parallelogram(b, h):
    return b*h


def sa_cylinder(r, h):
    return (2*3.14*r*h) + (2*3.14*(r**2))


def sv_cylinder(r, h):
    return 3.14*(r**2)*h


x = 2
y = 4
z = 5
r = 4
h = 2

print("Trapezoid Area:", trapezoid(x, y, h))
print("Parallelogram Area:", parallelogram(x, h))
print("Surface Area of Cylinder:", sa_cylinder(r, h))
print("Volume of Cylinder:", sv_cylinder(r, h))