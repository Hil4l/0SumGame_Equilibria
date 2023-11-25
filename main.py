"""
(n x m) payoff matrix M specifies a two-person zero-sum game.
Let the two players be R (for rows) and C (for columns).
Mij = k, the payoff due to R by C when R chooses strategy i and C chooses strategy j.

Dependencies: scipy, numpy
"""
import numpy as np
from payoff_matrix import PayoffMatrix
from binary_nor_tree import LEFT, RIGHT, BinaryNorTree
from matrix_tree_generator import MatrixTreeGenerator

def main():
    # M = np.array([
    #     [3, -1],
    #     [-2, 1]
    # ])
    # pm = PayoffMatrix(M)
    
    # r_strat = pm.compute_row_strat()
    # c_strat = pm.compute_col_strat()
    # print(f"row: {r_strat} / col: {c_strat}")
    
    #----------------------------------
    
    # k = 2
    # I = [0,0,1,1]        
    # A = [LEFT, RIGHT, LEFT]
    # tree = BinaryNorTree(k, A, I)
    # print("probes = ", tree.evaluate())
    
    #----------------------------------
    
    k = 1
    gen = MatrixTreeGenerator(k)
    print(gen.zero_one_permutations(8))

if __name__ =='__main__':
    main()
