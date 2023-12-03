from payoff_matrix import PayoffMatrix
from matrix_tree_generator import MatrixTreeGenerator
import os

# Dependencies: scipy, numpy

def main():
    
    # compute --------------
    k = 1
    gen = MatrixTreeGenerator(k)
    M = gen.generate_matrix()
    
    pm = PayoffMatrix(M)
    r_z, r_strat = pm.compute_row_strat()
    c_z, c_strat = pm.compute_col_strat()
    
    # display --------------
    os.system('cls')
    print(f"--------- ROW player ---------")
    print(f"z: {" "*6} {r_z}")
    print(f"strategy: {[p for p in r_strat]} ({len(r_strat)}) \n(sum = {sum(r_strat)})")
    print()
    print(f"--------- COL player ---------")
    print(f"z: {" "*6} {c_z}")
    print(f"strategy: {[p for p in c_strat]} ({len(c_strat)}) \n(sum = {sum(c_strat)})")    
       
    # rand_avg = pm.compute_rand_avg_complexity(100000)
        
if __name__ =='__main__':
    main()


# ---------- Matrice enonce ----------
# import numpy as np
# M = np.array([
# [3, -1],
# [-2, 1]
# ]) 


# ---------- Arbre enonce ----------
# k = 2
# I = [0,0,1,1]        
# A = [LEFT, RIGHT, LEFT]
# tree = BinaryNorTree(k, A, I)
# print("probes = ", tree.evaluate())