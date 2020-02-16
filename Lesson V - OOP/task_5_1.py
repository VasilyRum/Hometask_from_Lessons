"""
Разработать класс Complex, которые бы описывал комплексные числа,
позволял их складывать, вычитать, умножать, делить и получать модуль.
"""
import math


class Complex:
    """
Class that allow to do math with complex numbers
    """

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        """Return the sum of numbers."""
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """Return the sub of numbers."""
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """Return the multiplication of numbers."""
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        """Return the division of numbers."""
        real = ((self.real * other.real + self.imag * other.imag)
                / (other.real ** 2 + other.imag ** 2))

        imag = ((self.imag * other.real - self.real * other.imag)
                / (other.real ** 2 + other.imag ** 2))

        return Complex(real, imag)

    def __str__(self):

        return f'{self.real:.2f} - {abs(self.imag):.2f}i' \
            if self.imag < 0 \
            else f'{self.real:.2f} + {self.imag:.2f}i'

    def mod(self):
        """Return the module of number."""
        return f'{math.sqrt(self.real ** 2 + self.imag ** 2):.2f}'


RE, IM = map(int, input("Enter first number separated by space: ").split())
NUM1 = Complex(RE, IM)
RE, IM = map(int, input("Enter second numbers separated by space: ").split())
NUM2 = Complex(RE, IM)

print(f"Sum: {NUM1 + NUM2}")
print(f"Difference: {NUM1 - NUM2}")
print(f"Product: {NUM1 * NUM2}")
print(f"Quotient: {NUM1 / NUM2}")
print(f"Modules: {NUM1.mod()}, {NUM2.mod()}")
