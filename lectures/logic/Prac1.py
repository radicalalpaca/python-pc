# -*- coding: utf-8 -*-
"""
MATH2042 Practical 1:
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
    __doc__!  This can be useful in big projects, for example.
    Note that it's an attribute of the class itself, rather than any
    individual object."""

    def __init__(self, cats, dogs):
        # We'll pass the lists of pet names when we create a PetFamily object
        self.cats = cats
        self.dogs = dogs

    def talkaboutcats(self):
        print(f"My first cat is named {self.cats[0]}")


class ParseTreeNode:
    """A class whose objects represent nodes in a parse tree for a formula of 
    propositional logic.
    
    Data attributes should be among label, child, secondchild, parent."""

    def __init__(self, symbol):
        # Initialise the node with the given label
        self.label = symbol
        self.childrencount = 0
        self.parent = None

    def assignchild(self, givennode):
        if self.childrencount == 0:
            self.child = givennode
            self.childrencount += 1
        else:
            self.secondchild = givennode
        givennode.parent = self

    def subformula(self):  # Work in progress!
        # We'll use the symbols - for not, > for implies, v for or,
        # and & for and.
        if self.label == '-':
            return '(-' + self.child.subformula() + ')'
        elif self.label == "v":
            return "(" + self.child.subformula() + " v " + self.secondchild.subformula() + ")"
        elif self.label == "&":
            return "(" + self.child.subformula() + " & " + self.secondchild.subformula() + ")"
        elif self.label == ">":
            return "(" + self.child.subformula() + " > " + self.secondchild.subformula() + ")"
        else:
            return self.label  # This is what we want in the case of a leaf
            # In other cases it's wrong, but at least it won't cause the
            # program to crash while we're testing the code.


def parsetree(formula):
    current_node = ParseTreeNode("")  # dummy node
    for character in formula:
        if character == "(":
            new_node = ParseTreeNode("")
            current_node.assignchild(new_node)
            current_node = new_node
        elif character == ")":
            current_node = current_node.parent
        else:
            current_node.label = character
    return current_node.child


# Set up the nodes for the parse tree of the formula (-((pvr)&(q>r))) here (Q6)

print(parsetree("(-(((p)v(r))&((q)>(r))))").subformula())

# n1 = ParseTreeNode("-")
# n2 = ParseTreeNode("&")
# n3 = ParseTreeNode(">")
# n4 = ParseTreeNode("v")
# n5 = ParseTreeNode("q")
# n6 = ParseTreeNode("r")
# n7 = ParseTreeNode("p")
# n8 = ParseTreeNode("r")
#
# n1.assignchild(n2)
# n2.assignchild(n3)
# n2.assignchild(n4)
# n3.assignchild(n5)
# n3.assignchild(n6)
# n4.assignchild(n7)
# n4.assignchild(n8)
#
# print(n1.subformula())
