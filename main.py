# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("sohadezzat")
print("sohadezzat")
print("jalhoum")


# Function to add two numbers
def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def sub(num1, num2):
    return num1 - num2


# Function to divide two numbers
def div(num1, num2):
    if num2 != 0:#تجنب للخطأ
       return num1 / num2


# Function to multiply two numbers
def mul(num1, num2):
    return num1 * num2

#test
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Sum:", add(num1, num2))
print("Subtract:", sub(num1, num2))
print("Division:", div(num1, num2))
print("Multiplication:", mul(num1, num2))
