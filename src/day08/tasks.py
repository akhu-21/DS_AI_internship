import numpy as np
a= np.array([[1,2,2],[1,8,9]])
b= np.array([[10,20,30]])
result = a+b
print(result)

arr = np.random.rand(100)
squared = arr ** 2
print(squared[0:30])



a = np.array([[1,2]])
b = np.array([[3,4]])
vstacked = np.vstack((a,b))
hstacked = np.hstack((a,b))
print(vstacked)
print(hstacked)

data = np.array([[10,20,30],[40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))



print("Task 1: The Normalizer (Broadcasting & Stats)")
scores = np.random.randint(50,101,size=(5,3))
subject_mean = scores.mean(axis=0)
centred_scores = scores - subject_mean
print("original scores:\n",scores)
print("\nsubject-wise mean:\n",subject_mean)
print("\ncentered scores(fairly campred scores):\n",centred_scores)













print("Task 2: The Reshaper (Array Manipulation)")

data = np.arange(24)
reshaped_data = data.reshape(4, 3, 2)
final_data = reshaped_data.transpose(0, 2, 1)
print("Final Shape:", final_data.shape)
print("Final Array:\n", final_data)















