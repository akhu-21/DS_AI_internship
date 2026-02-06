# # simple calculator
# num1=int(input("Enter num1: "))
# num2=int(input("Enter num2: "))
# operation = input("Enter operation (+, -, *, /, **, %): ")
# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2

# elif operation == "/":
#     result = num1 / num2
# elif operation == "**":
#     result = num1 ** num2
# elif operation == "%":
#     result = num1 % num2
# print("Result:", result)
# # f string.
# name = "akhil"
# msg = "good morning"
# print(f"hello {msg}  everyone ,myself {name}")
# name = "akhil"
# age = 20
# is_student = True
# print(type(name))
# print(type(age))
# print(type(is_student))






############################################task-1##############################
name = input("Enter your name : ")
age = float(input("enter age : "))
age =int(age)  
new_age = 4 + age 
print(f"hey {name}, you will be {new_age} years old in 2030") 
############################################# task-2 ##############################
amount = float(input("enter amount : "))
people = int(input("enter number of people : "))
share = amount / people
print(f'Total Bill : {amount}. Each person pays: {share}')
########################################### task-3 #####################################
item_name="Mobile"
quantity=4
price=1999.98
in_stock=True
print("item:",item_name,", Qty:",quantity,", Price:",price,", Available:",in_stock)
total_cost=quantity*price
print("Total Cost: ",total_cost)