import random
import math
import matplotlib.pyplot as plt


def gen_uniform(theta: float) -> float:
    return random.uniform(0, 1) * theta


th = 12
n = 1000
Y = list()
for i in range(n):
    Y.append(gen_uniform(th))

Func=Y
for i in range(n):
    Func[i]/=th
plt.plot(Func,'o')
plt.show()