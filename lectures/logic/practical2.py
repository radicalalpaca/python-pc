variables = set()  # Set of variables which must be true if the formula is satisfiable.


def is_satisfiable(formula):
    """Takes a propositional formula in conjunctive normal form and returns
    true if formula is satisfiable along with a list of literals satisfying
    the formula, and false if formula is not satisfiable. Uses the DPLL
    algorithm. Formulas are represented by lists; each variable is represented
    by an integer 1, 2, 3, .... The negation of each variable is represented by
    -1, -2, -3, .... Each conjunct is a list of integers.

    :param list formula: Propositional formula in conjunctive normal form
    :return: Tuple (Boolean, list)
    :rtype: tuple
    """
    if len(formula) == 0:
        #  If there are no conjuncts, then the formula is true.
        true_variables = [variable for variable in variables if variable >= 1]
        #  If negation is true, then the variable is false.
        return True, true_variables
    for i in range(len(formula)):
        #  Iterates through each conjunct.
        if len(formula[i]) == 0:
            #  If a conjunct has no literals, then it is false.
            return False
        if any([-literal in formula[i] for literal in formula[i]]):
            #  If a variable and its negation are both in a conjunct, then
            #  the conjunct is true and can be cancelled.
            formula.remove(formula[i])
        if len(formula[i]) == 1:
            #  Unit propagation
            variables.add(formula[i][0])  # The literal must be true.
            for conjunct in formula:
                if -formula[i][0] in conjunct:
                    #  Removes the negation from each conjunct.
                    conjunct.remove(-formula[i][0])
            formula.remove(formula[i])  # Removes the literal.
            return is_satisfiable(formula)
        for literal in formula[i]:
            #  Iterates through each literal in the conjunct.
            if all([-literal not in conjunct for conjunct in formula]) and literal in variables:
                #  Pure literal elimination.
                variables.add(literal)  # Assume the literal must be true.
                for conjunct in formula:
                    # Iterates through all conjuncts and cancels if it contains the literal
                    if literal in conjunct:
                        formula.remove(conjunct)
                return is_satisfiable(formula)
            for conjunct in formula:
                if literal in conjunct and -literal not in variables:
                    # Assumes literal is true and removes all conjuncts containing the literal.
                    formula.remove(conjunct)
                    variables.add(literal)  # Adds true literal to list of true variables.
                    return is_satisfiable(formula)
