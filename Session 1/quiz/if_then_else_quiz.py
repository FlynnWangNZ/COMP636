# Question 1
# ACDEF


# Question 2
def compare(v1, v2):
    if v1 > v2:
        return v1
    elif v1 < v2:
        return v2
    else:
        return "these values are equal"


# Question 3
def bool_test(input_var):
    return bool(input_var)


# Question 4
def type_check(input_var):
    common_str = "this variable type is: "
    if type(input_var) == str:
        type_str = "String"
    elif type(input_var) == int:
        type_str = "Integer"
    elif type(input_var) == float:
        type_str = "Float"
    elif type(input_var) == list:
        type_str = "List"
    
    return common_str + type_str
