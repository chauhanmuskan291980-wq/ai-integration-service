import math
course = "        Python Programming     "
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.find("Pro"))
print(course.replace("P","J"))
print("Pro" in course)


print(10 + 1)
print(10 - 1)
print(10 * 1)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x=10
x = x+3
x +=3
print(x)
 

print(round(2.9))
print(round(2.4))
print(abs(-2.9))
print(math.ceil(2.2))
x1 = input("x:")
print(x1)
y = int(x1) + 1
print(y)



# what are the pprimitive types in python 
# strings , Int , Boolean 

fruit = "Apple"
print(fruit[1])  #p
print(fruit[1:-1])

print(bool("False"))


temperature = 3
if temperature > 30:
    print("It's warm")
    print("Drink Water")
elif temperature < 20 and temperature > 10:
    print("It's nice")
else:
    print("It's cold")
print("Done")

high_income = True
good_credit = False

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")


high_income = True
good_credit = False
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")


high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
