"""
Solve the following Linear Problem:

    max z

    z - X*A0 ≤ 0       equ: z ≤ X*A0
    ...
    z - X*An ≤ 0

    sum(X) = 1 
    X ≥ 0
"""

import numpy as np
from scipy.optimize import linprog

class PayoffMatrix:
    def __init__(self, M) -> None:
        self.M = M
    
    def compute_row_strat(self):
        """
        Solve linear problem assoiated to playoff matrix M: max min (Payoffs) for player R
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
        Solve linear problem assoiated to playoff matrix M: max min (Payoffs) for player C
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
    
    def _lp_solve(self, c, A_ub, b_ub, A_eq, b_eq, bounds):
        result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

        z = - result.fun # Negate the result for maximization
        P = result.x
        strategy = P[1:] # variables without z
        return strategy