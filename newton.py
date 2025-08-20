import numpy as np
def first_deriv(f, x, epsilon = 0.0001): 
    """ 
    Parameters
    ----------
    f: function to differentiate
    x: a variable
    epsilon: to estimate
    """
    return (f(x+epsilon)-f(x))/epsilon
def sec_deriv(f, x, epsilon = 0.0001):
    """ 
    Parameters
    ----------
    f: function to differentiate
    x: a variable
    epsilon: to estimate
    """
    return (f(x+epsilon)-2*f(x)+f(x-epsilon))/(epsilon**2)
    

def optimize(start, fun, epsilon = 0.0001):
    """ 
    Parameters
    ----------
    start: starting value 
    fun: function to minimize
    epsilon: smallest difference between x_t and x_t_1
    """
    x_t_1 = start
    first = first_deriv(fun, x_t_1, epsilon) 
    sec = sec_deriv(fun, x_t_1, epsilon)
    for i in range(10000):
        if sec == 0: # if the second derivative is 0, stop the loop
            break
        x_t = x_t_1 - first/sec # Newton's method
        if np.linalg.norm(x_t - x_t_1) < epsilon: # stop when their abs value is less than epsilon
            break
    return x_t

