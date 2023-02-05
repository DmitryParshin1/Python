# In[7]:


print('ку-ку')


# In[8]:


h = 0
while h < 10:
    h += 1


# In[10]:


x = 2


# In[11]:


x


# In[12]:


x + 12


# In[13]:


x = 11
y = 22
x + y


# In[17]:


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

fib(10)


# In[20]:


fib(12)


# In[21]:


li = []
for i in range(1,10):
    li.append(i)
li


# In[22]:


fibs = [(n, fib(n)) for n in range(1,10)]
fibs


# In[23]:


from math import sqrt

def solve(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return (x1, x2)
    else:
        return 'Вещественных корней нет'


# In[24]:


solve(0.5,0.125,0)


# In[25]:


solve(1,2,3)


# In[26]:


z1 = complex(1,2)
z2 = complex(3,5)
z1, z2
# (z1, z2)


# In[27]:


'z1 = ({}, {})'.format(z1.imag, z2.real)


# In[32]:


import cmath

def csolve(a, b, c):
    d = b**2 - 4*a*c
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    return (x1, x2)


# In[33]:


csolve(1, 2, 5)


# In[34]:


f = lambda x: x**3
list(map(f, range(1,5)))


# In[35]:


import matplotlib.pyplot as plt
import random

# random.randint(1,10)

vx = [1.0,2.0,3.0]
vy = [1.0,2.0,1.0]

sx = vx[0]
sy = vy[0]

px = []
py = []

for i in range(1,1000):
    r = random.randint(0,2)
    sx = (sx + vx[r]) / 2
    sy = (sy + vy[r]) / 2
    px.append(sx)
    py.append(sy)
    
plt.plot(px, py, 'o')
plt.show()


# In[37]:


import matplotlib.pyplot as plt
import random

count = 3
x = list(range(1, 7))
y = [0 for i in x]

fig, ax = plt.subplots()

for _ in range(count):
    y[random.randint(0, 5)] += 1
    
ax.bar(x, y)
#
y.sort()
#print('{}%'.format(round((y[5] - y[0] / count * 100, 3)))
stat = [f'{i+1}: {round (y[i] / count * 100)}%' for i in range(0,6)]
print(stat)
plt.show


# In[38]:


from sympy import *
from sympy.plotting import plot
init_printing()


# In[39]:


x = Symbol('x')


# In[40]:


f = x + 2022
f


# In[41]:


f.subs(x, -77)


# In[42]:


f.subs(x, -210)


# In[43]:


plot(f)
print(f)


# In[44]:


g = sin(x+x)/x
plot(g)
print(g)


# In[45]:


h = x**2
h


# In[46]:


plot(h)
print(h)


# In[47]:


h=-h


# In[48]:


plot(h)
print(h)


# In[49]:


a = 1
b = 0
c = 0
h = a*x**2 + b*x+c
h


# In[55]:


a = 1
b = 3
c = 4
h = a*x**2 + b*x+c
h


# In[56]:


plot(h)
print(h)


# In[57]:


solve(h, x)


# In[53]:


q = x/(x+2)
q


# In[58]:


plot(q)


# In[59]:


fun1 = plot(q,(x,-10,-2.1), show=False)
fun2 = plot(q,(x,-1.9,10), show=False)
fun1.append(fun2[0])
fun1.show()


# In[60]:


x = Symbol('x')


# In[61]:


y = 1*x**2 + 2*x - 10
solve(y)


# In[62]:


res = plot(y,(x,-5,5))


# In[80]:


#Дана функция f(x) = 5*x**2 + 10*x - 30
#4. Построить график
#1. Определить корни
#5. Вычислить вершину
#2. Найти интервалы, на которых функция возрастает
#3. Найти интервалы, на которых функция убывает
#6. Определить промежутки, на котором f > 0
#7. Определить промежутки, на котором f < 0


# In[121]:


import numpy as np
import matplotlib.pyplot as plt


# In[122]:


limit = 10
step = 0.01


# In[123]:


a, b, c = 5, 10, -30


# In[124]:


x = np.arange(-limit, limit, step)


# In[125]:


def func(x):
    return a*x**2 + b*x + c


# In[126]:


def take_roots(a, b, c):
    discr = b**2 - 4*a*c
    if discr > 0:
        x1 = (-b + discr**0.5)/(2*a)
        x2 = (-b - discr**0.5)/(2*a)
        return x1, x2
    elif discr == 0:
        x = -b / (2*a)
        return x, x
    else:
        return None, None


# In[127]:


roots = take_roots(a, b, c)


# In[128]:


#print(take_roots(5, 10, -30))
#print(np.roots([5, 10, -30])) то же самое roots - вычесляет корни


# In[129]:


min_y = (min(func(x)))
min_x = take_roots(a, b, c - min_y)[0]


# In[130]:


#x_down = np.arange(-limit, min_x, step)
#x_up = np.arange(min_x, limit, step)


# In[131]:


x_down_pos = np.arange(-limit, min(roots), step)
x_down_neg = np.arange(min(roots), min_x, step)
x_up_neg = np.arange(min_x, max(roots), step)
x_up_pos = np.arange(max(roots), limit, step)


# In[141]:


plt.rcParams['lines.linestyle'] = '-'
plt.plot(x_down_pos, func(x_down_pos), 'r', label = 'Убывание выше 0')
plt.plot(x_up_pos, func(x_up_pos), 'b', label = 'Возрастание выше 0')
plt.rcParams['lines.linestyle'] = '--'
plt.plot(x_down_neg, func(x_down_neg), 'r', label = 'Убывание ниже 0')
plt.plot(x_up_neg, func(x_up_neg), 'b', label = 'Возрастание ниже 0')
plt.plot(roots[0], func(roots[0]), 'go', label =f'Корни ({round(min(roots),2)}, {round(max(roots),2)})')
plt.plot(roots[1], func(roots[1]), 'go')
plt.plot(min_x, min_y, 'cx', label =f'Экстремум ({min_x}, {min_y})')
plt.grid()
plt.legend()


# In[ ]:


#Дана функция f(x) = 5*x**2 + 10*x - 30
#4. Построить график
#1. Определить корни
#5. Вычислить вершину
#2. Найти интервалы, на которых функция возрастает
#3. Найти интервалы, на которых функция убывает
#6. Определить промежутки, на котором f > 0
#7. Определить промежутки, на котором f < 0

