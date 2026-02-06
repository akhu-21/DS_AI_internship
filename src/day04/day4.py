student = {
    "name" : "akhil",
    "class" : 12
}
student["age"]=20
student["city"]="hospet"
print(student)
print(type(student))
print(student.get("age"))
marks={"maths": 80 , "science": 75 , "english": 85}
for subject, score in marks.items():
    print(subject,score)

marks.update({"history": 90})  
print(marks)

purchases = {

    "alice": 120,
    "bob": 85,
    "charlie": 200
}
for person, amount in purchases.items():
    print(f"{person}: used ${amount}")

n = int(input("enter number of customers:"))
user_purchases= {}
for i in range(n):
    name = input("enter customer name:")
    amount = int(input("enter purchase amount:"))
    user_purchases[name] = amount
    print("customer purchases data:",user_purchases)


top_customer = max(user_purchases, key=user_purchases.get)
print("Top customer:", top_customer)

lowest_customer = min(user_purchases, key=user_purchases.get)
print("lowest customer:", lowest_customer)
a = {1, 2, 3,}
b = {3,4,5}
print(a|b)
print(a&b)
print(5 in a)
print(5 in b)

############################### task-1 (contact book)############################

print("task-1")

contacts = {
    "akhil": 9742170774,
    "prakash": 8861481506,
    "lakshmi": 9036536318
}
contacts["renu"] = 7795530380
contacts["bhimu"] = 9980306919 

existing_contact = contacts.get("akhil", "Contact not found")
non_existing_contact = contacts.get("rahul", "Contact not found")
print("Safe Lookup Results:")
print("akhil:", existing_contact)
print("rahul:", non_existing_contact)

print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")

############################### task-2 (The "Duplicate Cleaner" (Sets))############################

print("task-2")

IDs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
print(f"raw IDs: {IDs}")
unique_users = set(IDs)
print(f'unique_users: {unique_users}')
print("ID05" in unique_users)
length = len(IDs)
set_length = len(unique_users)
duplicates_removed = length - set_length
print(f'duplicates_removed: {duplicates_removed}')

##################### task-3 (The Interest Matcher (Set Operations))############################

print("task-3")

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print(f'intersection: {friend_a & friend_b}')
print(f'union: {friend_a | friend_b}')
print(f'difference (friend_a - friend_b): {friend_a - friend_b}')