# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt


def bandit(mu, sigma, k, t, epsilon):
    q = np.random.normal(mu, sigma, k)  # generate true q's
    a_best = np.argmax(q)
    Q = np.zeros(k)  # initialize Q vector
    Qlist = []  # the vector for storing the rewards
    for i in range(t):
        u = np.random.uniform(0, 1, 1)  # sample from uniform distribution
        if u <= epsilon:
            a = np.random.choice(10, 1)
        else:
            a = np.argmax(Q)
        a = np.argmax(Q)
        R = np.random.normal(q[a], 1, 1)  # reward
        Qlist.append(R)  # get reward
        Q[a] += 1 / (i + 1) * (R - Q[a])
    return q, Q, Qlist


def run(n,epsilon):
    y = np.zeros(1000)
    for i in range(n):
        res = bandit(0, 1, 10, 1000, epsilon)
        y = np.add(y, np.array(res[2]))
    return np.divide(y, n)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    y1 = run(2000, 0)
    y2 = run(2000, 0.01)
    y3 = run(2000, 0.1)
    plt.plot(range(1000), y1)
    plt.plot(range(1000), y2)
    plt.plot(range(1000), y3)
    plt.show()
