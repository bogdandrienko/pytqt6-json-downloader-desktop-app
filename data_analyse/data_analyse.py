import random

import matplotlib.pyplot as plt
import numpy as np


def start():
    x = sorted([random.randint(1, 1000) for x in range(1, 100)])
    y = sorted([random.randint(1, 200) for x in range(1, 100)])
    xpoints = np.array(x)
    print("x max: ", xpoints.max(initial=1))
    ypoints = np.array(y)
    print("y min: ", ypoints.min(initial=1))

    plt.plot(xpoints, ypoints)
    plt.show()


if __name__ == '__main__':
    pass
