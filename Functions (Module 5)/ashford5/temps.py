# Phillip Ashford 2510522 COP 1000

def c_to_f(celsius_temp):
    fahrenheit = (celsius_temp * 9/5) + 32
    print(f'{celsius_temp} Celsius equals {fahrenheit:.1f} Fahrenheit')

def f_to_c(fahrenheit_temp):
    celsius = (fahrenheit_temp - 32) * 5/9
    return celsius
