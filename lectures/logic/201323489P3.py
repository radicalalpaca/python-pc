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
        self.child = None
        self.secondchild = None
        self.label = None

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
    """Flattens a nested list using recursion.
    Source: https://stackoverflow.com/a/17867797

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


def split_formula(string_formula):
    """Takes a formula string and splits it at the base connective. Counts
    brackets to determine this.

    :param string string_formula: Propositional formula in string form
    :return: Formulas on left and right of central connective
    :rtype: tuple
    """
    bracket_count = 0
    i = 0
    for character in string_formula:
        i += 1
        if character == "(":
            bracket_count += 1
            continue
        elif character == ")":
            bracket_count -= 1
        if bracket_count == 1:
            # When number right brackets minus left brackets is one, we know
            # we're at the central connective.
            return string_formula[1:i], string_formula[i + 1:-1]


def join_formula(string1, string2, connective):
    """Connects two formulas over a given connective.

    :param string string1: Formula on left of connective
    :param string string2: Formula on right of connective
    :param string connective: Connective
    :return: Joined formula
    """
    return "(" + string1 + connective + string2 + ")"

class ProofTreeNode:
    """Class that represents a node in a proof tree.

    :param ParseTreeNode node: Parsetreenode formula
    """
    def __init__(self, node):
        self.formula = node
        self.premises = None
        self.consequence = None
        self.NDRule = None
        self.count = 0

    def assignpremises(self, premise_list):
        """Assigns a given list of premises to the node, and assigns the node as the
        consequence of each premise

        :param list premise_list: List of nodes above the current node in the tree.
        """
        self.premises = premise_list
        for premise in premise_list:
            # loops through each premise, assigning current node as its consequence.
            premise.consequence = self

    def numnodesupward(self):
        """Returns the total number of nodes, including the current node, above the
        current node.

        :return: Number of nodes at and above the node
        :rtype: int
        """
        num_nodes = 1  # includes current node
        for premise in self.premises:
            # Loops through each premise
            if isinstance(premise, ProofTreeNode):
                # If node is a proof tree node, then it will have more nodes above it,
                # so use recursively run method again
                num_nodes += premise.numnodesupward()
            else:
                # Else it is a parse tree node, therefore it has no nodes above it
                num_nodes += 1
        return num_nodes

    def assumptions(self):
        """Returns a list of all the assumptions at or above the node in the proof tree.

        :return: List of assumptions
        :rtype: list
        """
        assumption_list = []
        for premise in self.premises:
            if isinstance(premise, ParseTreeNode):
                # If node is just a parse tree node, then there is nothing
                # above it, so it must be a premise.
                assumption_list.append(premise.Subformula())
            else:
                # Else it is a proof node, so recursively run this method
                assumption_list.append(premise.assumptions())
        return flatten(assumption_list)

    def assignNDRule(self, rule):
        """Assigns the given string as the natural deduction rule for the node.
        Possibles rules are: -I, -E, &I, &EL, &ER, vIL, vIR, vE, >I, >E, EFQ and RAA.

        :param str rule: Natural deduction rule
        """
        self.NDRule = rule

    def Subformula(self):
        """Returns string formula of proof tree node.

        :return: string formula
        :rtype: str
        """
        return self.formula.Subformula()

    def UndischargeAssumptions(self):
        """Returns set of undischarged assumptions of the node.

        :return: undischarged assumptions
        :rtype: set
        """
        undischarged_assumptions = self.assumptions()
        if self.NDRule == "-I":
            # If rule is NOT introduction, then discharges the negation of the formula from the assumptions.
            return set(undischarged_assumptions.remove(self.Subformula()[2:-1]))
        elif self.NDRule == ">I":
            # If rule is IMPLIES introduction, then discharges antecedent of formula.
            return set(undischarged_assumptions.remove(split_formula(self.Subformula())[0]))
        elif self.NDRule == "vE":
            # If rule is OR elimination, then discharges both formulas of the disjunction
            statement = ""
            for premise in self.premises:
                if premise.Subformula() != self.Subformula():
                    statement = premise.Subformula()
            undischarged_assumptions.remove(split_formula(statement)[0])
            undischarged_assumptions.remove(split_formula(statement)[1])
            return set(undischarged_assumptions)
        elif self.NDRule == "RAA":
            # In reductio ad absurdum, discharges the negation of the formula.
            undischarged_assumptions.remove("(-" + self.Subformula() + ")")
            return set(undischarged_assumptions)
        else:
            # For all other rules, no assumptions are discharged.
            return set(undischarged_assumptions)

    def isValid(self):
        """Checks if the proof tree at and above the node is valid.

        :return: True if proof tree is valid, false otherwise
        :rtype: bool
        """
        global i  # Makes the counter global, so we can modify it locally.
        if self.NDRule is None:
            # 7(a): Every node that isn't a leaf node must have a deduction rule.
            return False
        elif self.NDRule == "-I":
            # In NOT introduction, checks if premise is falsum, if so then checks the proof of
            # the falsum is valid.
            if self.premises[0].Subformula() == "(F)":
                i += 1
                self.premises[0].isValid()
            else:
                return False
        elif self.NDRule == "-E":
            # In NOT elimination, makes sure formula is falsum, and checks if above premises are
            # negations of each other. Here the [2:-1] list slice removes the negation.
            if self.Subformula() == "(F)":
                if (
                    self.premises[0].Subformula()[2:-1] == self.premises[1].Subformula()
                    or self.premises[1].Subformula()[2:-1] == self.premises[0].Subformula()
                ):
                    #  Both premises are checked for validity.
                    i += 1  # Adds one to the counter for each node checked
                    if isinstance(self.premises[0], ProofTreeNode):
                        # Checks if premise is itself a proof
                        self.premises[0].isValid()
                    else:
                        #  Else it is just a premise, and adds one to the counter for this node.
                        i += 1
                    if isinstance(self.premises[1], ProofTreeNode):
                        self.premises[1].isValid()
                    else:
                        i += 1
                else:
                    return False
            else:
                return False
        elif self.NDRule == "&I":
            # And introduction, checks if the premises are equal to the conjunction when split up.
            if list(split_formula(self.Subformula())) == self.premises:
                # Both premises are checked for validity.
                i += 1
                if isinstance(self.premises[0], ProofTreeNode):
                    self.premises[0].isValid()
                else:
                    i += 1
                if isinstance(self.premises[1], ProofTreeNode):
                    self.premises[1].isValid()
                else:
                    i += 1
            else:
                return False
        elif self.NDRule == "&EL":
            # AND elimination, checks if formula on the left of the premise conjunction is equal to the
            # current node.
            if self.Subformula() == split_formula(self.premises[0].Subformula())[0]:
                i += 1
                if isinstance(self.premises[0], ProofTreeNode):
                    self.premises[0].isValid()
                else:
                    i += 1
            else:
                return False
        elif self.NDRule == "&ER":
            # AND elimination, checks if formula on the right of the premise conjunction is equal to the
            # current node.
            if self.Subformula() == split_formula(self.premises[0].Subformula())[1]:
                i += 1
                if isinstance(self.premises[0], ProofTreeNode):
                    self.premises[0].isValid()
                else:
                    i += 1
            else:
                return False
        elif self.NDRule == "vIL":
            # Checks if formula on left side of OR is equal to the premise above.
            if split_formula(self.Subformula())[0] == self.premises[0].Subformula():
                i += 1
                if isinstance(self.premises[0], ProofTreeNode):
                    self.premises[0].isValid()
                else:
                    i += 1
            else:
                return False
        elif self.NDRule == "vIR":
            # Checks if formula on right side of OR is equal to the premise above.
            if split_formula(self.Subformula())[1] == self.premises[0].Subformula():
                i += 1
                if isinstance(self.premises[0], ProofTreeNode):
                    self.premises[0].isValid()
                else:
                    i += 1
            else:
                return False
        elif self.NDRule == "vE":
            # OR elimination, checks if current node is equal to two out of the three premises.
            if (
                self.Subformula() == self.premises[0].Subformula()
                and self.Subformula() == self.premises[1].Subformula()
            ):
                # Checks if both both premises are valid.
                i += 1
                if isinstance(self.premises[0], ProofTreeNode):
                    self.premises[0].isValid()
                else:
                    i += 1
                if isinstance(self.premises[1], ProofTreeNode):
                    self.premises[1].isValid()
                else:
                    i += 1
            elif (
                self.Subformula() == self.premises[0].Subformula()
                and self.Subformula() == self.premises[2].Subformula()
            ):
                # Checks if both both premises are valid.
                i += 1
                if isinstance(self.premises[0], ProofTreeNode):
                    self.premises[0].isValid()
                else:
                    i += 1
                if isinstance(self.premises[2], ProofTreeNode):
                    self.premises[2].isValid()
                else:
                    i += 1
            elif (
                self.Subformula() == self.premises[1].Subformula()
                and self.Subformula() == self.premises[2].Subformula()
            ):
                # Checks if both both premises are valid.
                i += 1
                if isinstance(self.premises[1], ProofTreeNode):
                    self.premises[1].isValid()
                else:
                    i += 1
                if isinstance(self.premises[2], ProofTreeNode):
                    self.premises[2].isValid()
                else:
                    i += 1
            else:
                return False
        elif self.NDRule == ">I":
            # IMPLIES introduction. Checks if the premise is the consequent of the current node.
            if split_formula(self.Subformula())[1] == self.premises[0].Subformula():
                i += 1
                if isinstance(self.premises[0], ProofTreeNode):
                    self.premises[0].isValid()
                else:
                    i += 1
            else:
                return False
        elif self.NDRule == ">E":
            # IMPLIES elimination. Checks if one the premises is the antecedent of the other premise,
            # and that the current node is the consequent of that premise.
            if (
                self.Subformula() == split_formula(self.premises[1].Subformula())[1]
                and self.premises[0].Subformula() == split_formula(self.premises[1].Subformula())[0]
            ):
                i += 1
                if isinstance(self.premises[0], ProofTreeNode):
                    self.premises[0].isValid()
                else:
                    i += 1
                if isinstance(self.premises[1], ProofTreeNode):
                    self.premises[1].isValid()
                else:
                    i += 1
            elif (
                self.Subformula() == split_formula(self.premises[0].Subformula())[1]
                and self.premises[1].Subformula() == split_formula(self.premises[0].Subformula())[0]
            ):
                i += 1
                if isinstance(self.premises[0], ProofTreeNode):
                    self.premises[0].isValid()
                else:
                    i += 1
                if isinstance(self.premises[1], ProofTreeNode):
                    self.premises[1].isValid()
                else:
                    i += 1
            else:
                return False
        elif self.NDRule == "EFQ":
            # ex falso quodlibet, checks if premise is falsum.
            if self.premises[0].Subformula() == "(F)":
                i += 1
                self.premises[0].isValid()
            else:
                return False
        elif self.NDRule == "RAA":
            # reductio ad absurdum
            if self.premises[0].Subformula() == "(F)":
                i += 1
                self.premises[0].isValid()
            else:
                return False
        if i == self.numnodesupward():
            # If the total number of nodes checked is equal to the total number of nodes
            # at or above the current node, and function hasn't returned false at all,
            # then 7(b) is satisfied
            return True


    def StatementofProof(self):
        """If proof is valid, returns statement in form of
        undischarged assumptions |- formula

        :return: Invalid or statement of proof
        :rtype: str
        """
        output_string = "{"
        if self.isValid():
            # If proof is valid, then appends each undischarged assumption into a string.
            for assumption in self.UndischargeAssumptions():
                output_string += (assumption + ", ")
            print(output_string + " } |- " + self.Subformula())
        else:
            print("Invalid")


fstring1 = '(-((p)&((q)>(r))))'
fstring2 = '(p)'
fstring3 = '(-(p))'
fstring4 = '(F)'

formula1 = ParseTree(fstring1)
formula2 = ParseTree(fstring2)
formula3 = ParseTree(fstring3)
formula4 = ParseTree(fstring4)

Proof1 = ProofTreeNode(formula4)
Proof1.assignpremises([formula2, formula3])
Proof1.assignNDRule("-E")

Proof2 = ProofTreeNode(formula2)
Proof2.assignpremises([formula3, formula1])

i = 0  # counter variable for isValid method

print(Proof1.StatementofProof())