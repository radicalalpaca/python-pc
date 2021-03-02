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
