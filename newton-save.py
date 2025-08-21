import numpy as np
def first_deriv(f, x, epsilon = 0.0001):
    return (f(x+epsilon)-f(x))/epsilon
def sec_deriv(f, x, epsilon = 0.0001):
    return (f(x+epsilon)-2*f(x)+f(x-epsilon))/(epsilon**2)
    

def optimize(start, fun):
    x_t_1 = start
    epsilon = 0.0001
    first = first_deriv(fun, x_t_1, epsilon)
    sec = sec_deriv(fun, x_t_1, epsilon)
    for i in range(10000):
        if sec == 0:
            break
        x_t = x_t_1 - first/sec
        if np.linalg.norm(x_t - x_t_1) < epsilon:
            break
    return x_t