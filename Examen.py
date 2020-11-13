import numpy as np


A = np.array([[400, 6, -250, 10],[6, -82, 40, -35],[-250, 40, 370, 14],[10, -35, 14, 370]])
b = np.array([1, 1, 1, 1])

D = np.array([[400, 6, 0, 0],[6, -82, 40, 0],[0, 40, 370, 14],[0, 0, 14, 370]])
E = np.array([[0, 0, -250, 10],[0, 0, 0, -35],[-250, 0, 0, 0],[10, -35, 0, 0]])

T = -np.linalg.inv(D) * E
p_T = np.linalg.norm(T, ord=2)
print(T)
print(p_T)

