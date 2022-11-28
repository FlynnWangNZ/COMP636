# Question 1
def function_name(variable_input):
     variable_output = variable_input + " world!"
     return variable_output


# Question 2
def double_input(input_str):
    return input_str * 2


# Question 3
def multiple_input(var1: int, var2: list):
    print(var2)
    return var2[var1]


# Question 4
def square_times(var_one, var_two):
    return var_one ** 2 * var_two


# Question 5
def uniques(var1: list):
    print(var1)
    return set(var1)


# Question 6
def accel_finder(mass, force):
    acceleration = force / mass
    return acceleration


# Question 7
def test_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


