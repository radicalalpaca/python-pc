# -*- coding: utf-8 -*-
"""
MATH2042 Practial Solutions 1a:
    Object Oriented Programming.

Lecturer: Andrew Brooke-Taylor
"""

class PetFamily:
    """A simple example of a class.
    
    Describes a family of pets, with a list 'dogs' of (names of) dogs and
    a list 'cats' of cats.
    
    By the way, this is called a documentation string. 
    It's different from a comment that you get using a #, in that you
    can actually access it in the run-time: it's a data attribute named
    __doc__!  This can be useful in big projects, for example."""
    
    def __init__(self, cats, dogs):
        # We'll pass the lists of pet names when we create a PetFamily object
        self.cats = cats
        self.cats.append("The Stray")
        self.dogs = dogs
    
    def talkaboutcats(self):
        print ('My first cat is named', self.cats[0])


class Cheese:
    """A class of objects with no defined methods."""


class ParseTreeNode:
    """A class whose objects represent nodes in a parse tree for a formula of 
    propositional logic.
    
    Data attributes should be among label, child, secondchild, parent,
    and childrencount."""
    
    def __init__(self,givenlabel):
        # Initialise the node with the given label
        self.label = givenlabel
        self.childrencount = 0
        
    def assignChild(self,givennode):
        """Sets givennode to be the (first) child of self if there are
        currently no children, or the secondchild otherwise.  Note:
        doesn't handle well cases where the user tries to assign further
        children."""
        if self.childrencount == 0:
            self.child = givennode
        else:
            self.secondchild = givennode
        self.childrencount = self.childrencount + 1
        
                    
    def Subformula(self):
        """Returns the subformula at the present node, as defined in 
        Example 2.2.8 of the lecture notes.""" 
        # We'll use - for not, > for implication, v for or, and & for and.
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

        
n1 = ParseTreeNode('-')
n2 = ParseTreeNode('&')
n3 = ParseTreeNode('v')
n4 = ParseTreeNode('>')
n5 = ParseTreeNode('p')
n6 = ParseTreeNode('r')
n7 = ParseTreeNode('q')
n8 = ParseTreeNode('r')
n1.assignChild(n2)
n2.assignChild(n3)
n2.assignChild(n4)
n3.assignChild(n5)
n3.assignChild(n6)
n4.assignChild(n7)
n4.assignChild(n8)

    



