### Week 1: Python Fundamentals I - Day 2: Exercises

1.  **Simple Calculation:** Write a program that calculates the sum, difference, product, and quotient of two numbers entered by the user. Print all the results with clear labels.

    ```python
    # Exercise 1 Solution (example - solutions will be provided separately to learners after they try)
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")

    num1 = float(num1_str) # Use float to handle decimal input
    num2 = float(num2_str)

    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2

    print(f"Sum: {num1} + {num2} = {sum_result}")
    print(f"Difference: {num1} - {num2} = {difference_result}")
    print(f"Product: {num1} * {num2} = {product_result}")
    print(f"Quotient: {num1} / {num2} = {quotient_result}")
    ```

2.  **Area of a Triangle:** Write a program to calculate the area of a triangle. Take the base and height as input from the user (you can assume they are integers or floats).  Area of triangle = (1/2) \* base \* height.

    ```python
    # Exercise 2 Solution (example)
    base_str = input("Enter the base of the triangle: ")
    height_str = input("Enter the height of the triangle: ")

    base = float(base_str)
    height = float(height_str)

    area = 0.5 * base * height

    print(f"Area of the triangle with base {base} and height {height} is: {area}")
    ```

3.  **Temperature Conversion:** Write a program to convert temperature from Celsius to Fahrenheit. Take the temperature in Celsius as input. Formula: Fahrenheit = (Celsius \* 9/5) + 32.

    ```python
    # Exercise 3 Solution (example)
    celsius_str = input("Enter temperature in Celsius: ")
    celsius = float(celsius_str)

    fahrenheit = (celsius * 9/5) + 32

    print(f"{celsius}°C is equal to {fahrenheit}°F")
    ```

4.  **Swap Variables:** Write a program to swap the values of two variables without using a temporary variable. (Hint: You can use simultaneous assignment in Python).

    ```python
    # Exercise 4 Solution (example)
    var1 = 10
    var2 = 20

    print(f"Before swapping: var1 = {var1}, var2 = {var2}")

    var1, var2 = var2, var1 # Simultaneous assignment for swapping

    print(f"After swapping: var1 = {var1}, var2 = {var2}")
    ```

5.  **Circle Properties:** Write a program to calculate the circumference and area of a circle given its radius. Use `pi = 3.14159`.  Circumference = 2 \* pi \* radius, Area = pi \* radius \* radius.

    ```python
    # Exercise 5 Solution (example)
    radius_str = input("Enter the radius of the circle: ")
    radius = float(radius_str)
    pi = 3.14159

    circumference = 2 * pi * radius
    area = pi * radius ** 2

    print(f"Circle with radius {radius}:")
    print(f"Circumference = {circumference:.2f}") # Format to 2 decimal places
    print(f"Area = {area:.2f}") # Format to 2 decimal places
    ```

---

**Daily Simple Task:**
### Daily Simple Task - Day 2

Write a program to calculate the area of a rectangle using variables and operators.

```python
# Daily Simple Task Solution (example)
length_str = input("Enter the length of the rectangle: ")
width_str = input("Enter the width of the rectangle: ")

length = float(length_str)
width = float(width_str)

area = length * width

print(f"The area of the rectangle with length {length} and width {width} is: {area}")