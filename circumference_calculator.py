def calculate_circumference(radius):
    pi = 3.14159  
    circumference = 2 * pi * radius
    return circumference

# Get user input for the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the circumference
circumference = calculate_circumference(radius)

# Display the result
print(f"The circumference of the circle with radius {radius} is: {circumference:.2f}")
