# -*- coding: utf-8 -*-
"""
MATH2042 Practial Solutions 1b:
    Object Oriented Programming.

Lecturer: Andrew Brooke-Taylor
"""

class ParseTreeNode:
    """A class whose objects represent nodes in a parse tree for a formula of 
    propositional logic.
    
    Data attributes should be among label, child, secondchild, parent,
    and childrencount."""
    
    def __init__(self):
        self.childrencount = 0
        
    def assignChild(self,givennode):
        """Sets givennode to be the (first) child of self if there are
        currently no children, or the secondchild otherwise.  Also
        sets the parent of givennode to be the current node.  
        Note: doesn't handle well cases where the user tries to assign further
        children."""
        if self.childrencount == 0:
            self.child = givennode
        else:
            self.secondchild = givennode
        self.childrencount = self.childrencount + 1
        givennode.parent = self
    
    def assignLabel(self,givenlabel):
        """Sets the label of the node to be givenlabel."""
        self.label = givenlabel
                    
    def Subformula(self):
        """Returns the subformula at the present node, as defined in 
        Example 2.2.8 of the lecture notes.""" 
        # We'll use - for not, > for impication, v for or, and & for and.
        if self.label == '-':
            return '(-'+self.child.Subformula()+')'
        elif self.label == '&':
            return '('+self.child.Subformula()+' & '+self.secondchild.Subformula()+')'
        elif self.label == 'v':
            return '('+self.child.Subformula()+' v '+self.secondchild.Subformula()+')'
        elif self.label == '>':
            return '('+self.child.Subformula()+' > '+self.secondchild.Subformula()+')'
        else:
            return self.label # This is what we want in the case of a leaf


def ParseTree(formula):
    """Given a formula in the format described in ParseTreeAlgorithm.pdf
    (i.e. as per the lecture notes, but with an extra pair of parentheses 
    around each propositional variable or constant), returns the root node
    of the parse tree of the formula."""
    
    #The variable cn will denote the "current node".  
    #We create a dummy node to start with.
    cn = ParseTreeNode()
    
    for char in formula:
        if char == '(':
            newnode = ParseTreeNode()
            cn.assignChild(newnode)
            cn = newnode
        elif char == ')':
            cn = cn.parent
        else:
            cn.assignLabel(char)

    #At the end of that for loop, cn will be back pointing at the dummy
    #node above the real root node.
    return cn.child


    



