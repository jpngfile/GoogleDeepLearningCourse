import numpy as np
import matplotlib.pyplot as plt

scores = [3.0, 1.0, 0.2]

def softmax_helper(lst):
    exp_list = np.exp(lst)
    exp_sum = np.sum(exp_list)
    return np.array([(val/exp_sum) for val in exp_list])

def softmax(x):
    """
    Compute softmax values for each set of scores in x.
    """
    return np.apply_along_axis(softmax_helper, 0, x)

print(softmax(scores))

# Plot softmax curves
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
