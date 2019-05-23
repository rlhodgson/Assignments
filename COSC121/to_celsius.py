def to_celsius(fahrenheit):
    """Return the given fahrenheit temperature in degrees celsius"""
    degrees = (fahrenheit - 32) * 5 / 9
    return degrees

degrees = to_celsius(32.0)
print(degrees)
degrees = to_celsius(212.0)
print(degrees)
