def age_next_year(age):
    """Return a person's age next year given their age this year"""
    next_years_age = age + 1
    return next_years_age

print(age_next_year(10))
print(age_next_year(23))
print(age_next_year(99))


def to_celsius(temp_f):
    """Converts a given fahrenheit temperature to celsius"""
    return (temp_f - 32) * 5 / 9

print(to_celsius(212))
print(to_celsius(32))


def celsius(temp_f):
    """Converts a given fahrenheit temperature to celsius"""
    freezing = 32
    factor = 5 / 9
    ans = (temp_f - freezing) * factor
    return ans

print(celsius(212))
print(celsius(32))


 square = lambda x: x * x """means the same as squaring something"""