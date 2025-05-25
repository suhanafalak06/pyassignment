import math

class ShapeCalculator:
    def area(self, a=None, b=None):
        if a is not None and b is None:
            return math.pi * a * a
        elif a is not None and b is not None:
            return a * b
        else:
            return "Invalid input: Provide 1 or 2 arguments."
calc = ShapeCalculator()

circle_area = calc.area(5)            
rectangle_area = calc.area(4, 6)      
invalid = calc.area()                 

print(f"Area of Circle: {circle_area:.2f}")
print(f"Area of Rectangle: {rectangle_area}")
print(f"Invalid Case: {invalid}")