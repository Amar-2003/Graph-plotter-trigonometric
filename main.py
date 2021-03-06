import math
import matplotlib.pyplot as plt

e = input("Enter the function: ")
sums = e.split("+")
arrx = []
arry = []
x = -100
while(x < 100):
    arrx.append(x)
    val = 0
    for sum in sums:
        product = 1
        elements = sum.split("*")
        for element in elements:
            try:
                n = int(element)
                product *= n
            except:
                if(element == "sin"):
                    product *= math.sin(x)
                if(element == "cos"):
                    product *= math.cos(x)
        val += product
    x += 0.01
    arry.append(val)
plt.plot(arrx,arry)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Your graph")
plt.show()


    

