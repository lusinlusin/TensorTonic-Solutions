import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x)
    p = np.array(p)

    if abs(np.sum(p) - 1) < 10**(-6):
        return  np.sum(x * p)
    else:
        raise ValueError("probabilities don't sum to 1.")
    
