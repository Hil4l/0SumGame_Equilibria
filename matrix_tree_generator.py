from binary_nor_tree import BinaryNorTree
from itertools import product, islice
import numpy as np

class MatrixTreeGenerator:
    def __init__(self, k) -> None:
        self.k = k
    
    def generate_matrix(self):
        """
        Generate the payoff matrix from the "Game tree evaluation problem" derived 0-sum game binary NOR-tree of height 2k,
        by evaluating every combination of input i∈I and algorithm a∈A on the tree and encoding the resulting payoff in the corresponding cell (i,a)
        """
        n = 2**(self.k)       # {0,1}^4k (nodes on last level)
        m = 2**(self.k)-1     # {0,1}^(2^(2k)-1)) (all nodes until level height-1)
        inputs = self.zero_one_permutations(n)    
        algorithms = self.zero_one_permutations(m)
        
        rows = []
        for I in inputs:
            # populate row I with evaluation of the tree by each algorithm A
            row = [self.compute_cell_payoff(list(A), list(I)) for A in algorithms] # pass copies of I and A because used/modif in tree creation
            rows.append(row)
            
        M = np.array(rows) # convert to numpy matrix
        return M
    
    def compute_cell_payoff(self, A, I)-> int:
        """
        Generate the matrix cell M[i][j] by evaluating the Input (I) tree with the eval. algo. A
        """
        tree = BinaryNorTree(self.k, A, I)  # create (A,I) tree of height 2k
        payoff = tree.evaluate()            # evaluate tree
        return payoff
    
    def zero_one_permutations(self, n, limit=None):        
        """
        Generate all possible permutations of {0,1}^n
        used for I (n = 4k) and A (n = |internal nodes| = 2^(k+1)-1)
        """
        # limit slice not random (slice list, take first limit elements)
        
        alphabet = [0,1]                                            # {0,1}
        permutations = list(product(alphabet, repeat=n))          # all permutations
        limited_permutations = list(islice(permutations, limit))    # limited number (default all)
                
        return tupleList_to_listList(limited_permutations)
        

def tupleList_to_listList(ls):
    """
    convert a list of tuples to a list of lists by converting each tuple lement into a list
    (used in zero_one_permutations because I and A need to be mutable to build tree)
    """
    new_ls = [list(elem) for elem in ls]
    return new_ls

        
    