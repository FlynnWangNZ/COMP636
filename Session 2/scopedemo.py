local_variable = 7

print(local_variable)

local_variable = 8

def scope(x, y):
    # global local_variable
    local_variable = 11
    print(local_variable)

    function_variable = y
    
    def innerscope(x):
        inner_variable = x * 2
        print(function_variable)
        print(inner_variable)
        return inner_variable
    
    return function_variable + innerscope(x)


local_variable = 9
local_variable = scope(local_variable, 2)
print(local_variable)
