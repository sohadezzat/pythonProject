
def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')


    # Function to add two numbers
    def Sum(num1, num2):
        return num1 + num2


    # Function to subtract two numbers
    def sub(num1, num2):
        return num1 - num2


    # Function to divide two numbers
    def div(num1, num2):
        if num2 != 0:  # تجنب للخطأ
            return num1 / num2
# Function to multiply two numbers
def mul(num1, num2):
    return num1 * num2
def Calculate_triangle_area(base, height):
    return 0.5*base*height
def Calculate_circle_area(radius):
    return (radius*radius) * 3.14   #pi
def Calculate_rectangle_area(height, width):
    return height * width
list=['Sum','sub','div','mul','Calculate triangle area',' Calculate circle area','Calculate rectangle area','Exit']
print(list)
choice = input("Enter your choice: ")
if choice=='Sum':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Sum:", Sum(num1, num2))
elif choice=='sub':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("sub:", sub(num1, num2))
elif choice == 'div':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("div:", div(num1, num2))
elif choice == 'mul':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("mul:", mul(num1, num2))
elif choice == 'Calculate triangle area':
    base = int(input("Enter the base : "))
    height = int(input("Enter the height: "))
    print("triangle area:", Calculate_triangle_area(base, height))
elif choice == 'Calculate circle area':
    radius = int(input("Enter the radius: "))
    print("circle area:", Calculate_circle_area(radius))
elif choice == 'Calculate rectangle area':
    Length = int(input("Enter the Length: "))
    width = int(input("Enter the width : "))
    print(" rectangle area:", Calculate_rectangle_area(Length, width))
elif choice=='Exit':
    print('Exit')

