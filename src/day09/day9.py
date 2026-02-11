import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30,], index=['a', 'b', 'c'])

print(s1)
print(s2)

marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math', 'Chemistry']])


scores = pd.Series([45, 67, 89, 34, 90])

passed = scores[scores > 60]
print(passed)


data = pd.Series([10, None, 30, None])

print(data.isnull())
print(data.fillna(0))


names = pd.Series(['Alice', 'bob', 'CHARLIE'])

print(names.str.lower())
print(names.str.contains('a'))


print("Task 1: The Product Catalog (Series Creation & Indexing)")


products = pd.Series([700,150,300], index=['laptop', 'mouse', 'keyboard'])
laptop_price = products['laptop']
print("Laptop Price :", laptop_price)
print(products[['laptop','mouse']])
print(products)
print(products[0:2])

print("Task 2: The Grade Filter (Boolean Masking & Missing Data)")


grades = pd.Series([85, None, 92, 45, None, 78, 55])
missing_val = grades.isnull()
print(missing_val)

missing_val = grades.fillna(69)
print(missing_val)

score = grades[grades>60]
print(score)

print(grades)


print("Task 3: The Username Formatter (Vectorized String Operations)")

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print(usernames.str.strip())
print(usernames.str.lower())
print(usernames.str.contains("a"))
print(usernames)




























































