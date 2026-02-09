from django.urls import reverse
from numpy import sort


A= [1, 2, 3, 4, 5,6,7,8,9]
coordinates = (5,10)
print(numbers)
print(coordinates
print(A[-3:-1])
print(A[-7:-2:3])
A.sort(reverse=True)
print(A) 
########################### task-1 (list oprations)###################
print("task-1")
 inventory_containing = ["Apples", "Dates","Bananas", "Carrots"]
print(inventory_containing)

inventory_containing.append("eggs")
print(inventory_containing)

inventory_containing.remove("Bananas")
print(inventory_containing)

inventory_containing.sort()
print(inventory_containing)

########################### task-2(sliceing)###################
print("task-2")
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print(temperatures[0])
print(temperatures[-1])
print(temperatures[3:6])
print(temperatures[-3:])

########################### task-3(tuples) ###################
print("task-3(tuples opration)")
screen_res = (1920, 1080)
print(screen_res)

screen_res[0] = (1280)   #This line would raise an error because tuples are immutable
print(screen_res)

print("tuples cannot be modidifed")
