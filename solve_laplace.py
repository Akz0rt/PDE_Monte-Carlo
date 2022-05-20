import itertools
import pandas as pd

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def solve_heat(l,h,a=1):
    dx = 1
    X = np.zeros((int(l/dx)+1,int(h/dx)+1)) #матриця, що відображає початковий розподіл температури у області
    for x in np.arange(0, l+dx, dx):
        for y in np.arange(0,h+dx, dx):
            X_ar = np.full((10000,2),x)
            T = np.zeros(10000)
            for i in range(0, 10000):   #момент виходу оберемо 10000, адже за таку кількість кроків процес майже напевно вийде за межі області
                if i == 0:
                    X_ar[i] = [x,y]
                elif X_ar[i-1][0] <= 0 and X_ar[i-1][1] in range(0,h):
                    for k in range(i-1, 10000):
                        X_ar[k] = [0,y]
                        T[k]=boundary_1(y)
                    break
                elif X_ar[i-1][1] <= 0 and X_ar[i-1][0] in range(0,l):
                    for k in range(i-1, 10000):
                        X_ar[k] = [x,0]
                        T[k]=boundary_2(x)
                    break
                elif X_ar[i-1][0] >= l and X_ar[i-1][1] in range(0,h):
                    for k in range(i-1, 10000):
                        X_ar[k] = [l,y]
                        T[k] = boundary_3(y)
                    break
                elif X_ar[i-1][1] >= h and X_ar[i-1][0] in range(0,l):
                    for k in range(i-1, 10000):
                        X_ar[k] = [x,h]
                        T[k] = boundary_4(x)
                    break
                elif X_ar[i-1][0] <= 0 and X_ar[i-1][1] <= 0:
                    for k in range(i-1, 10000):
                        X_ar[k] = [0,0]
                        T[k] = boundary_1(0)
                    break
                elif X_ar[i-1][0] >= l and X_ar[i-1][1] >= h:
                    for k in range(i-1, 10000):
                        X_ar[k] = [l,h]
                        T[k] = boundary_3(h)
                    break
                elif X_ar[i-1][0] <= 0 and X_ar[i-1][1] >= h:
                    for k in range(i-1, 10000):
                        X_ar[k] = [0,h]
                        T[k] = boundary_1(0)
                    break
                elif X_ar[i-1][0] >= l and X_ar[i-1][1] <= 0:
                    for k in range(i-1, 10000):
                        X_ar[k] = [l,0]
                        T[k] = boundary_3(h)
                    break
                else:
                    X_ar[i]=[X_ar[i-1][0] + (a**2)*np.random.randn(),X_ar[i-1][1] + (a**2)*np.random.randn()] #моделювання одного кроку процесу
            X[int((l-x)/dx)][int((h-y)/dx)]=T[-1]
    return X
def boundary_1(y):
    b1 = eval(b_1)
    return b1
def boundary_2(x):
    b2 = eval(b_2)
    return b2
def boundary_3(y):
    b3 = eval(b_3)
    return b3
def boundary_4(x):
    b4 = eval(b_4)
    return b4


 
                

                    

if __name__ == '__main__':
    b_1 = input('Перша гранична умова: ')
    b_2 = input('Друга гранична умова: ')
    b_3 = input('Третя гранична умова: ')
    b_4 = input('Четверта гранична умова: ')
    l = 10
    h = 10
    a = 1.32
    
    M = 100
    n = len(solve_heat(l,h))
    E = np.zeros((l+1,h+1))
    for i in range(M):
        E += solve_heat(l, h, a=a)
    E = E/M
    df = pd.DataFrame(E)
    plt.figure(figsize=(7.5, 6.3))
    ax = plt.contourf(df, cmap='magma')
    plt.savefig('heatmap.png', dpi=800)
    plt.show()
