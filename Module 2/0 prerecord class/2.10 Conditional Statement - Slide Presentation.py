# Function to determine the type of a triangle
def determine_triangle_type(a, b, c):
    # Check if the sides can form a triangle
    if a + b > c and a + c > b and b + c > a:
        # Check for equilateral triangle
        if a == b == c:
            return "Equilateral triangle"
        # Check for isosceles triangle
        elif a == b or b == c or a == c:
            return "Isosceles triangle"
        # Otherwise, it's a scalene triangle
        else:
            return "Scalene triangle"
    else:
        return "Not a triangle"

# Example usage
side1 = 3
side2 = 4
side3 = 5

triangle_type = determine_triangle_type(side1, side2, side3)
print(f"The triangle with sides {side1}, {side2}, and {side3} is a {triangle_type}.")
