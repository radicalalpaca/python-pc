# -*- coding: utf-8 -*-
"""
Leo Collins
MATH2042 Practial 3.

Lecturer: Andrew Brooke-Taylor
"""


class ParseTreeNode:
    """A class whose objects represent nodes in a parse tree for a formula of
    propositional logic.

    Data attributes should be among label, child, secondchild, parent,
    and childrencount."""

    def __init__(self):
        self.childrencount = 0
        self.parent = None

    def assignChild(self, givennode):
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

    def assignLabel(self, givenlabel):
        """Sets the label of the node to be givenlabel."""
        self.label = givenlabel

    def Subformula(self):
        """Returns the subformula at the present node, as defined in
        Example 2.2.8 of the lecture notes, except with an extra pair of
        brackets around each occurrence of a  propositional variables or the
        falsum constant.

        We use - for not, > for impication, v for or, & for and,
        and F for the "falsum" constant symbol."""
        if self.label == '-':
            return '(-' + self.child.Subformula() + ')'
        elif self.label == '&':
            return '(' + self.child.Subformula() + '&' + self.secondchild.Subformula() + ')'
        elif self.label == 'v':
            return '(' + self.child.Subformula() + 'v' + self.secondchild.Subformula() + ')'
        elif self.label == '>':
            return '(' + self.child.Subformula() + '>' + self.secondchild.Subformula() + ')'
        else:
            return '(' + self.label + ')'  # This is what we want in the case of a leaf


def ParseTree(formula):
    """Given a formula in the format described in ParseTreeAlgorithm.pdf
    (i.e. as per the lecture notes, but with an extra pair of parentheses 
    around each propositional variable or constant), returns the root node
    of the parse tree of the formula."""

    # The variable cn will denote the "current node".
    # We create a dummy node to start with.
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

    # At the end of that for loop, cn will be back pointing at the dummy
    # node above the real root node.
    return cn.child


def flatten(nested_list):
    """Flattens a nested list.

    :param list nested_list: Nested list
    :return: Flattened list
    """
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(flatten(i))
        else:
            flat_list.append(i)
    return flat_list


class ProofTreeNode:
    """Class that represents a node in a proof tree.

    :param ParseTreeNode node: Parsetreenode formula
    """

    def __init__(self, node):
        self.formula = node
        self.premises = None
        self.consequence = None
        self.NDRule = None

    def assignpremises(self, premise_list):
        self.premises = premise_list
        for premise in premise_list:
            premise.consequence = self

    def numnodesupward(self):
        num_nodes = 1
        for premise in self.premises:
            if isinstance(premise, ProofTreeNode):
                num_nodes += premise.numnodesupward()
            else:
                num_nodes += 1
        return num_nodes

    def assumptions(self):
        assumption_list = []
        for premise in self.premises:
            if isinstance(premise, ParseTreeNode):
                assumption_list.append(premise.Subformula())
            else:
                assumption_list.append(premise.assumptions())
        return flatten(assumption_list)

    def assignNDRule(self, rule):
        self.NDRule = rule

    def isValid(self):
        if self.NDRule == None:
            return False
        else:
            for premise in self.premises:
                if isinstance(premise, ProofTreeNode):
                    if premise.NDRule == None:
                        return False
                    elif premise.NDRule == "-I":

                    elif premise.NDRule == "-E":

                    elif premise.NDRule == "&I":

                    elif premise.NDRule == "&EL":
                        if premise.formula.Subformula() in premise.premises[0]:
                            premise.premises[0].isvalid()
                        else:
                            return False
                    elif premise.NDRule == "&ER":
                        if premise.formula.Subformula() in premise.premises[0]:
                            premise.premises[0].isvalid()
                        else:
                            return False
                    elif premise.NDRule == "vIL":

                    elif premise.NDRule == "vIR":

                    elif premise.NDRule == "vE":

                    elif premise.NDRule == ">I":

                    elif premise.NDRule == ">E":
                        if (premise.premises[0].Subformula() and premise.formula.Subformula()) in premise.premises[1]:
                            premise.premises[1].isValid()

                    elif premise.NDRule == "EFQ":

                    elif premise.NDRule == "RAA":

                else:
                    continue





fstring1 = '(-((p)&((q)>(r))))'
fstring2 = '(p)'
fstring3 = '(-(p))'
fstring4 = '(F)'

formula1 = ParseTree(fstring1)
formula2 = ParseTree(fstring2)
formula3 = ParseTree(fstring3)
formula4 = ParseTree(fstring4)

Proof1 = ProofTreeNode(formula2)
Proof2 = ProofTreeNode(formula4)

Proof2.assignpremises([formula1, formula2])
Proof1.assignpremises([Proof2, formula3])

print(Proof1.assumptions())