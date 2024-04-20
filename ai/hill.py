def hill_climbing(f, x0, delta=0.1):
    x = x0
    while True:
        # generate neighbors of x
        neighbors = [x + delta * d for d in [-1, 1]]
        # find the neighbor with the highest function value
        best_neighbor = max(neighbors, key=f)
        if f(best_neighbor) <= f(x):
            return x
        x = best_neighbor

# define the function to optimize
def f(x):
    return -x**2 + 10

# find the maximum value of f in the range [-10, 10]
x_opt = hill_climbing(f, 0)
print(f"The maximum value of f is {f(x_opt)} at x = {x_opt:.2f}")