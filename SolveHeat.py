import numpy as np
import matplotlib.pyplot as plt

def u_start(x):
    u0 = eval(start)
    return u0
def boundary_1(t):
    b1 = eval(b_1)
    return b1
def boundary_2(t):
    b2 = eval(b_2)
    return b2

def solve_heat(l, dt, t, a=1):
    n = t/dt
    dx = l/100
    X = []
    for x in np.arange(0, l+dx, dx):
        X_ar = np.full(int(n),x)
        T = np.zeros(int(n))
        for i in range(0, int(n)):
            if i == 0:
                X_ar[i] = x
            elif X_ar[i-1] <= 0:
                for k in range(i-1, len(X_ar)):
                    X_ar[k] = 0
                    T[k] = boundary_1(t-(i-1)*dt)
                break
            elif X_ar[i-1] >= l:
                for k in range(i, len(X_ar)):
                    X_ar[k] = l
                    T[k] = boundary_2(t-(i-1)*dt)
                break
            else:
                X_ar[i] = X_ar[i-1] + (a**2)*np.sqrt(dt)*np.random.randn()
                T[i] = u_start(X_ar[i])
        if X_ar[-1] <= 0:
            X_ar[-1] = 0
        elif X_ar[-1] >= l:
            X_ar[-1] = l
        X.append(T[-1])
    return X
                  

if __name__ == '__main__':
    start = input('Введіть вираз, що описує початковий розподіл температури: ')
    b_1 = input('Перша гранична умова: ')
    b_2 = input('Друга гранична умова: ')
    l = 50
    a = 1.32
    dt = 0.01
    t = float(input("Розв'язок шукається у момент часу: "))
    M = 100000
    n = len(solve_heat(l, dt, t))
    X = np.empty(shape=(M,n))
    E = []
    fig = plt.figure(figsize=(12,8))
    axl = fig.add_subplot(111)
    for i in range(M):
        X[i] = solve_heat(l, dt, t, a=a)
    for i in range(n):
        s=0
        for j in range(M):
            s+=float(X[j][i])
        E.append(s/M)
    axl.plot(E, 'r')
    plt.show()

