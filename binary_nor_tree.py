"""
Game tree evaluation
- the two players are the input I (rows), and a set A of deterministic algorithms (columns)
- the payoff is the running time of the algorithm on the input (number of probes to the Input)

We consider zero-sum games derived from the Game tree evaluation problem in:
    a binary NOR-tree of height 2k
    
- the set I of inputs is the set of binary strings in {0, 1}^n with n = 4k
- the set A of deterministic recursive pruning algorithms, encoded by associating a child order bit to internal NOR nodes,
  indicating which of the 2 subtree is evaluated first.
- The complexity/payoff is the number of bits of the input probed by the algorithm (with NOR prunning).

-------------------------------------------------------
ex: k=1, I={0,0,1,1}, A = {0,1,0} (left, right, left)

            NOR
           //  \
         NOR    NOR
         / \\   // \
        0   0   1   1             
-------------------------------------------------------
"""

LEFT = 0
RIGHT = 1

class Node:
    def __init__(self, order=None, val=None):
        self.order = order  # (0|1) -> (left|right)
        self.val = val      # input bit
        
        self.left:Node = None
        self.right:Node = None
            
    def is_leaf(self):
        return self.val is not None
    
    def get_first_child(self):
        return self.left if self.order == LEFT else self.right
    
    def get_second_child(self):
        return self.left if self.order == RIGHT else self.right

class BinaryNorTree:
    def __init__(self, k, A, I) -> None:
        self.k = k
        self.root = self.build_tree(self.k, A, I) 
        
    def build_tree(self, k, A, I) -> Node:
        if k == 0:
            return Node(val=I.pop(0))  # leaf
        
        root = Node(order=A.pop(0))                # inner node (NOR)
        root.left = self.build_tree(k - 1, A, I)
        root.right = self.build_tree(k - 1, A, I)
        return root
    
    def evaluate(self):
        probes = [0] # mutable (to be modified by _evaluate)
        self._evaluate(self.root, probes)
        return probes[0]
    
    def _evaluate(self, node:Node, probes):
        
        if node is None: return None
    
        if node.is_leaf():
            probes[0] += 1
            return node.val

        # eval first child
        first_val = self._evaluate(node.get_first_child(), probes)
        
        # NOR-prunning (1 NOR 0|1 = 1)
        if first_val == 1:
            return 0
        
        # eval second child
        second_val = self._evaluate(node.get_second_child(), probes)
        return nor(first_val, second_val)

def nor(a, b) -> int:
    return 1 if (a == 0 and b == 0) else 0 