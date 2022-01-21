# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt

def bandit(mu, sigma, k, t):
    q = np.random.normal(mu, sigma, k)
    Q = np.zeros(k)
    Qlist = []
    for i in range(t):
        a = np.argmax(Q)   # best action
        Qlist.append(Q[a]) # reward at time i
        R = np.random.normal(q[a],1,1) # reward
        Q[a] += 1/(i+1)*(R - Q[a])
    return q,Q,Qlist

def run(n):
    y = np.zeros(1000)
    for i in range(n):
        res = bandit(0, 1, 10, 1000)
        y = np.add(y, np.array(res[2]))
    return np.divide(y,n)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Q = bandit(0,1,10,1000)
    y = run(2000)
    plt.plot(range(1000),y)
    plt.show()