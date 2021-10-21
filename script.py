import random

class Arbre(object):

    def __init__(self, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
    
    def __repr__(self):
        if self.left == None and self.right == None:
            return "()"
        else:
            return "(" + str(self.left) + "" + str(self.right) + ")" 
    def __str__(self) -> str:
        if self.left == None and self.right == None:
            return "()"
        else:
            return "(" + str(self.left) + "" + str(self.right) + ")"

    def set_left(self,left):
        self.left = left
    
    def set_right(self, right):
        self.right = right
    
    def get_parents(self, parent=None, parents={}):
        if self != None:
            parents[self] = parent
        parent = self
        if self.left != None:
            return self.left.get_parents(parent, parents)

        if self.right != None:
            return self.right.get_parents(parent, parents)
        return parents
    
    def count(self) -> int :

        if self.left == None and self.right == None:
            return 0
        else:
            if self.left != None and self.right!= None:
                return 1 + self.left.count() + self.right.count()
            else:
                if self.left == None:
                    return 1 + self.right.count()
                else:
                    return 1 + self.left.count()
    def count_leafs(self):
        if self.left == None and self.right == None:
            return 1 
        else:
            if self.left != None and self.right != None:
                return self.left.count_leafs() + self.right.count_leafs()
            elif self.left == None:
                return self.right.count_leafs()
            else:
                return self.left.count_leafs()

    def is_left_or_right(self, node):
        if self.left == node: return 1
        return 0

    @staticmethod
    def arbre2str(tree, filename="text.txt"):
        with open(filename, "w") as file:
            file.write(str(tree))

    @staticmethod
    def generate_tree_test(n):
        l = [Arbre(None, None, None) for _ in range(n)]
        parent = None
        while len(l) > 1:
            left = l.pop()
            right = l.pop()
            a = Arbre(left, right, parent)
            parent = a
            l.append(a)
        return l[0]
    

    @staticmethod
    def remy(n):
        # the first time the parent of the root sould be none abre de taille 1000 largeur 50 hauteur 100
        parent : Arbre = None
        tree = Arbre(None, None, parent=parent)
        parents = {}
        parents[tree] = parent
        new_tree_r, new_tree_l = None, None

        for _ in range(n):
            n_keys = len(parents)
            current_tree = list(parents.keys())[random.randint(0, n_keys-1)]
            parent = parents[current_tree]
            new_tree = Arbre()
            p = random.randint(0, 1)
            
            # case where the parent is none

            if parent == None:
                # current tree goes to the left
                if p == 1:
                    new_tree_r = Arbre()
                    new_tree.set_left(current_tree)
                    new_tree.set_right(new_tree_r)
                    parents[new_tree_r] = new_tree
                # current tree goes to the right
                else:
                    new_tree_l =  Arbre()
                    new_tree.set_right(current_tree)
                    new_tree.set_left(new_tree_l)
                    parents[new_tree_l] = new_tree
                parents[current_tree] = new_tree
                # becomes the root node with the parent None
                parents[new_tree] = None
            else:
                # in case the tree has a valide parent ie NOT NONE
                if p == 1:
                    new_tree_r = Arbre()
                    new_tree.set_left(current_tree)
                    new_tree.set_right(new_tree_r)
                    parents[new_tree_r] = new_tree
                    

                else:
                    new_tree_l = Arbre()
                    new_tree.set_right(current_tree)
                    new_tree.set_left(new_tree_l)
                    parents[new_tree_l] = new_tree
                   
                if parent.is_left_or_right(current_tree) == 1:
                    parent.set_left(new_tree)
                else:
                    parent.set_right(new_tree)
                parents[current_tree] = new_tree
                parents[new_tree] = parent
        
        for k, v in parents.items():
            if v == None:
                return k

if __name__ == "__main__":
    a = Arbre.remy(10)
    # k internal nodes and k + 1 leafs
    print(a.count(), a.count_leafs())