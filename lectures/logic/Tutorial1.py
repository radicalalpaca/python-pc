#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tutorial 1

@author: Andrew
"""

class PetFamily:
    """A class whose objects represent a pet family.
    Data attributes should include a list of cats, mycats
    and a list of dogs, mydogs."""
    
    def __init__(self, cats, dogs):
        self.mycats = cats
        self.mycats.append("The stray")
        self.mydogs = dogs
        
    def talkaboutcats(self):
        print ('My first cat is named ', self.mycats[0])
        
        
        
class ParseTreeNode:  #Work in Progress!
    """A class each object of which represents a node in the parse tree
    of a formula of Propositional Logic.
    
    Data attributes should include: child, secondchild, label, parent."""
    
    def __init__(self, symbol):
        self.label = symbol
        
    def assignparent(self, node):
        self.parent = node
        



