import numpy as np
#pip install numdifftools
import numdifftools as nd
def fun(x, y):
    return (x**2) + (y**2)
def multivariate(start, fun, epsilon = 0.00001):
    hessian = nd.Hessian(fun)
    gradient = nd.Gradient(fun)
    x_t_1 = np.array(start, dtype = float)
    x_t = x_t_1 - np.linalg.solve(hessian(x_t_1), gradient(x_t_1))
    #while np.linalg.norm(x_t - x_t_1) > epsilon:
    for _ in range(10000):
        h = hessian(x_t_1)
        g = gradient(x_t_1)
        try:
            x_t = x_t_1 - np.linalg.solve(h, g)
        except np.linalg.LinAlgError:
            break
        
        x_t_1 = x_t
    return x_t