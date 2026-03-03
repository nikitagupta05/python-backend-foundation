

def circle(radius):
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    return area, circumference

a,c = circle(2)
print(f"Area of a circle is {a} and circumference is {c}")