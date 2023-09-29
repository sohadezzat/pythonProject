#print(bool(0),bool(3.14),bool(1.0+1))
#print(-18//4)
#print(2%6)
# a = 4  # تمثيل بتي للرقم 5: 0101
# b = 11  # تمثيل بتي للرقم 3: 0011
#
# result_or = a | b  # الـ OR البتي
# result_shift = a >> 2  # تحريك البتات
#
# print(result_or)    # سيطبع: 7 (تمثيل بتي للرقم 7: 0111)
# print(result_shift) # سيطبع: 1 (تمثيل بتي للرقم 1: 0001)

# def max(a,b,c):
#     if a >= b and a >= c:
#        print(a)
#     elif b >= a and b >= c:
#         print(b)
#     else:
#         print(c)
# max(10,7,3)
# def factorial(n):
#     if n < 0:
#         print("non-negative integer")
#     elif n == 0:
#         print(1)
#     else:
#         print( n * factorial(n - 1))

# dictionary1 = {
#     "1": "present",
#     "2": "absent",
#     "3": "present",
#     "4": "absent",
# }
# def attendance(roll_number):
#     if roll_number in dictionary1:  #نفس list بمشي عليها بشرط المفتاح يكون موجود
#         return dictionary1[roll_number]# برجع القيمة المطابقة للمفتاح المدخل
#     else:
#         return "roll number not found"
# roll_number = input("Enter the roll number: ")
# attendance_status = attendance(roll_number)
# print(attendance_status)

def factorial(number):
    if number < 0:
        return "(non-negative integer)"
    elif number == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, number +1):#بزود واحد عشان اشمل الرقم الي دخله المستخدم
            factorial *= i
        return factorial

print(factorial(3))#1* 1*2* 3 ==6







# def reverse(your_string) :
#     reversed_string = ""
#     for character in reversed(your_string):#تعاملت مع الstring كlist وقلبته
#      reversed_string += character
#     return reversed_string
#
# your_string = input("Enter a string: ")
# print("Reversed string:", reverse(your_string))