import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return pow(x,4)-x*108+7
a = 2.
b = 3.
eps = 0.001 #точність 
 
def dihotom(a, b, eps): 
    while (abs(a-b) > eps):
        if f(a)*f((a+b)/2)<0: 
            b = (a+b)/2 
 
        else: 
            a = (a+b)/2
    
    print('Корінь рівняння x = ', round((a+b)/2))
dihotom(a,b,eps) 

x = np.arange(a, b, 0.01)
plt.plot(x, f(x)) 
plt.xlabel('x')  
plt.ylabel('f(x)') 
plt.title('Метод ділення навпіл')  
plt.grid() 
plt.show()