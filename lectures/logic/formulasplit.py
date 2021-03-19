fstring1 = "(((p)v((r)>(q)))&((r)v((p)&(q))))"
fstring2 = "((p)&(q))"
fstring3 = "((p)>((q)>(r)))"
fstring4 = "(-((p)&((q)>(r))))"
fstring5 = "(p)"
fstring6 = "(q)"

def split_formula(string_formula):
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
            return string_formula[1:i], string_formula[i + 1:-1]

def formula_negation(string_formula):
    return string_formula[2:-1]

def join_formula(string1, string2, rule):
    if rule == "&I":
        return "(" + string1 + "&" + string2 + ")"

def return_list(list):
    output_string = "{ "
    for element in list:
        output_string += (element + ", ")
    print(output_string + " } |- " + "q")

return_list(["gay", "tree", "shark"])
