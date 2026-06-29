#!/usr/bin/env python3

print("Welcome to Group 30 Calculator!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    return a % b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (add/subtract/multiply/divide/power/modulo): ").strip().lower()

if operation == "add":
    print(f"Result: {add(num1, num2)}")
elif operation == "subtract":
    print(f"Result: {subtract(num1, num2)}")
elif operation == "multiply":
    print(f"Result: {multiply(num1, num2)}")
elif operation == "divide":
    print(f"Result: {divide(num1, num2)}")
elif operation == "power":
    print(f"Result: {power(num1, num2)}")
elif operation == "modulo":
    print(f"Result: {modulo(num1, num2)}")
else:
    print("Bro what?! That is not even a math thing! Try add, subtract, multiply, divide, power or modulo!")

