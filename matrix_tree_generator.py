from binary_nor_tree import BinaryNorTree
from itertools import product, islice
import numpy as np

class MatrixTreeGenerator:
    def __init__(self, k) -> None:
        self.k = k
        
    def generate_cell_payoff(self, A, I)-> int:
        """
        Generate the matrix cell M[i][j] by evaluating the Input (I) tree with the eval. algo. A
        """
        height = self.k*2                   # height 2k
        tree = BinaryNorTree(height, A, I)  # create (A,I) tree of height k
        payoff = tree.evaluate()            # evaluate tree
        return payoff
    
    def generate_matrix(self):
        """
        Generate the payoff matrix from the "Game tree evaluation problem" derived 0-sum game binary NOR-tree of height 2k,
        by evaluating every combination of input i∈I and algorithm a∈A on the tree and encoding the resulting payoff in the corresponding cell (i,a)
        """
        n = self.k*4            # {0,1}^4k
        m = 2**(self.k+1)-1     # {0,1}^(2^(k+1)-1))
        Inputs = self.zero_one_permutations(n)    
        Algorithms = self.zero_one_permutations(m)
        
        M = np.array([])
        
        # for I in inputs
        #   row = []
        #   fro A in Algorithms
        #   M.add(row)
        i_a_payoff = self.generate_cell_payoff(Algorithms[0], Inputs[0])
        
        return M
    
    def zero_one_permutations(self, n, limit=None):        
        """
        Generate all possible permutations of {0,1}^n
        used for I (n = 4k) and A (n = |internal nodes| = 2^(k+1)-1)
        """
        # limit slice not random (slice list, take first limit elements)
        
        alphabet = [0,1]                                            # {0,1}
        permutations = list(product(alphabet, repeat=n, ))          # all permutations
        limited_permutations = list(islice(permutations, limit))    # limited number (default all)
            
        return limited_permutations
        
    
        
    