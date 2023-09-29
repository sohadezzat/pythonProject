# #Q1:
# personal_list = []
# number_people = int(input("Enter the number of people: "))
# for i in range(number_people):
#     personal_name = input(f"Enter the name {i+1}: ")
#     age = int(input(f"Enter the age of {i+1}: "))
#     gender = input(f"Enter the gender of {i+1}  Male or Female: ")
#     number_cities = int(input(f"Enter the number of cities for {i+1}: "))
#     city_list = []
#     for j in range(number_cities):
#         city_name = input(f"Enter city {j+1} for {i+1}: ")
#         city_list.append(city_name)
#     person_dic= {
#         "Name": personal_name,
#         "Age": age,
#         "Cities": city_list,
#         "Gender": gender
#     }
#     personal_list.append(person_dic)
# print(personal_list)
#Q2:
def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

try:
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    if length <= 0 or width <= 0:
        raise ValueError("Both length and width must be positive numbers")
    area = calculate_rectangle_area(length, width)
    perimeter = calculate_rectangle_perimeter(length, width)
    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")

except ValueError as e:
    print(f"Error: {e}")
