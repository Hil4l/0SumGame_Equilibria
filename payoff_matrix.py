import numpy as np
from scipy.optimize import linprog
import random as rand
class PayoffMatrix:
    def __init__(self, M) -> None:
        self.M = M
    
    def compute_row_strat(self):
        """
        Build linear problem (inequalities, objective) associated to playoff matrix M (Payoffs) for player Row
        and call _lp_solve to solve it
        return: results of the linear problem
        """
        n, m = self.M.shape
        c = [-1] + [0]*n  # objective function coeff (-z -> [-1, 0, 0, ..., 0])
        
        # Inequality constraints;
        temp = - np.transpose(self.M) # change equation side (≤) / transpose because work wihth Row playoffs from Col actions
        A_ub = np.column_stack((np.ones(m), temp)) # add column of 1s for z (z - ...)
        b_ub = [0]*m
        
        # Equality constraint (sum proba = 1)
        A_eq = [[0] + [1]*n]
        b_eq = [1]
        
        bounds = [(None, None)] + [(0, None)]*n
        
        return self._lp_solve(c, A_ub, b_ub, A_eq, b_eq, bounds)
    
    def compute_col_strat(self):
        """
        Build linear problem (inequalities, objective) associated to playoff matrix M (Payoffs) for player Col
        and call _lp_solve to solve it
        return: results of the linear problem
        """
        n, m = self.M.shape
        c = [-1] + [0]*m  # objective function coeff (-z -> [-1, 0, 0, ..., 0])

        # Inequality constraints; (no sign inversion -> both - cancel: 1st minus due to translation max-min / 2nd minus change equation side (≤))
        A_ub = np.column_stack((np.ones(n), self.M)) # add column of 1s for z (z - ...)
        b_ub = [0]*n

        # Equality constraint (sum proba = 1)
        A_eq = [[0] + [1]*m]
        b_eq = [1]

        bounds = [(None, None)] + [(0, None)]*m

        return self._lp_solve(c, A_ub, b_ub, A_eq, b_eq, bounds)
    
    def _lp_solve(self, c, A_ub, b_ub, A_eq, b_eq, bounds) -> tuple[int, list[tuple]]:
        """
        solve LP problem wth cipy.linprog
        return: tuple(z, p), with z the objective function value and p the best strategy (list of probabilities)
        """
        result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

        z = - result.fun # Negate the result for maximization
        P = result.x
        strategy = P[1:] # variables without z
        return z, strategy
    
    def compute_rand_avg_complexity(self, it_num:int):
        """
        randomly computes the average number of leaves probed using the payoff matrix
        return randomized average matrix value
        """
        res = 0
        for _ in range(it_num):
            i = rand.randint(0, len(self.M)-1)
            j = rand.randint(0, len(self.M[0])-1)
            val = self.M[i][j]
            res += val
        
        return res/it_num
