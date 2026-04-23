import matplotlib.pyplot as plt

x = [4, 8, 9, 2]
y = [3, 5, 2, 1]

x2 = [1, 2, 3, 6]
y2 = [2, 4, 6, 7]


#plt.plot(x,y)
plt.scatter(x,y)
plt.plot(x2,y2)

plt.title("Scatter Plot and Line Graph")
plt.xlabel("X Value")
plt.ylabel("Y Value")

plt.show()