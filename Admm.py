class Admm:
    def __init__(self, epsilon, rho, max_iter, A, b, C, d):
        self.epsilon = epsilon
        self.rho = rho
        self.max_iter = max_iter
