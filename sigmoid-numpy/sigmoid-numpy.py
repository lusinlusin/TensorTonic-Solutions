import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    v = np.array(x)
    r = 1/(1+ 1/np.exp(v))
    return r