class ParseTreeNode:
    """Class that represents a node in a parse tree for a propositional formula.

    :param string symbol: Either a propositional variable, or one of three connectives:
        NOT, OR, AND, IMPLY.
    """

    def __init__(self, symbol):
        self.label = symbol
        self.childrencount = 0  # Number of children. Either 0, 1 or 2.
        self.parent = None  # Parent of node. Initially empty.
        self.child = None  # Child of node. Initially empty.
        self.secondchild = None  # Second child of node. Initially empty.

    def assignchild(self, givennode):
        """Assigns a given node as child. If node already has one child, then given node
        is assigned as secondchild.

        :param ParseTreeNode givennode: Node to be assigned as child
        """
        if self.childrencount == 0:
            # If current node has no children, then new node is assigned
            # as first child.
            self.child = givennode
            self.childrencount += 1  # The current node now has 1 child.
        else:
            #  Else the new node is assigned as second child.
            self.secondchild = givennode
        givennode.parent = self  # Assigns the parent of the new node as current node.

    def subformula(self):
        """Returns the subformula of current node.

        :return: Subformula of node
        :rtype: string
        """
        if self.label == '-':
            # NOT label
            return '(-' + self.child.subformula() + ')'
        elif self.label == "v":
            # OR label
            return "(" + self.child.subformula() + " v " + self.secondchild.subformula() + ")"
        elif self.label == "&":
            # AND label
            return "(" + self.child.subformula() + " & " + self.secondchild.subformula() + ")"
        elif self.label == ">":
            # material conditional label
            return "(" + self.child.subformula() + " > " + self.secondchild.subformula() + ")"
        else:
            # leaf node
            return self.label


def parsetree(formula):
    """Parses plain text propositional formula into a parse tree. Formula
    must have brackets around each variable.

    :param string formula: Propositional formula in plain text.
    :return: Returns root node of parse tree.
    :rtype: ParseTreeNode
    """
    current_node = ParseTreeNode("")  # dummy node
    for character in formula:
        if character == "(":
            # Creates empty node and assigns it as the child of the previous node.
            new_node = ParseTreeNode("")
            current_node.assignchild(new_node)
            current_node = new_node
        elif character == ")":
            # Changes current node to its parent.
            current_node = current_node.parent
        else:
            # Assigns the current node the label of the character.
            current_node.label = character
    return current_node.child  # Loop ends on dummy node; returns child of dummy node.
