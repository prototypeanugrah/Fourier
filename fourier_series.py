"for a given function of your choice, enter function in line 17 and 19"

from pylab import *
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def four(f,n):
  
  a = []
  b = []
   
  for i in range (0,1+n):

    
    result,error = quad(lambda x: (x**2-2*x)*cos((2*pi*i*x)/(2*pi)) , -pi , pi)
    a.append(result/pi)
    result,error = quad(lambda x: (x**2-2*x)*sin((2*pi*i*x)/(2*pi)) , -pi , pi)
    b.append(result/pi)
    
  def fn(x):
    sum = a[0]/2
    for i in range(1, 1+n):
      sum = sum + a[i]*cos((2*pi*i*x)/(2*pi)) + b[i]*sin((2*pi*i*x)/(2*pi))
    return sum
  return fn

xs = np.linspace(-8, 8, 300)
plt.plot(xs, amap(four(f,10), xs))
plt.show()
