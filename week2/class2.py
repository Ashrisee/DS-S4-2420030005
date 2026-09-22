import matplotlib.pyplot as plt
y1 = []
y2 = []
x = range(-100, 100 , 10)
for i in x:y1.append(i**2)
for i in x:y2.append(-i**2)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("X")
plt.ylabel("Y")
plt.ylim(-2000, 2000)
plt.axhline(0)
plt.axvline(0)
plt.savefig("class2.png")
plt.show()
