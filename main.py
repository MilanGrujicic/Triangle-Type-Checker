def triangle_type(a, b, c):
    '''Checks if provided side lenghts form a triangle,
      and which type of triangle based on side and angle.'''
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle."
    elif a == b == c:
        return "Equilateral."
    elif a == b or a == c or b == c:
        if is_right_triangle(a, b, c):
            return "Isosceles and right."
        return "Isosceles."
    else:
        if is_right_triangle(a, b, c):
            return "Scalene and right."
        return "Scalene."

def is_right_triangle(a, b, c):
    '''Checks whether the given sides form a right-angled triangle.'''
    return (b**2 + a**2 == c**2)

if __name__ == "__main__":
    try:
        a = round(float(input("Enter the length of side a: ")), 2)
        b = round(float(input("Enter the length of side b: ")), 2)
        c = round(float(input("Enter the length of side c: ")), 2)

        if a <= 0 or b <= 0 or c <= 0:
            print("ERROR \nAt least one side is negative or zero.") 
        else:
            triangle = triangle_type(a, b, c)
            print('-=' * 20)
            print(f"The triangle is: {triangle}")

    except ValueError:
        print('-=' * 20)
        print("ERROR \nPlease enter valid positive numbers.")
    print("ERROR \nPlease enter valid positive numbers.")
