import inspect

# Get functions from a library
def enumerateLibraryFunctions(lib):
    return inspect.getmembers(lib, inspect.isfunction)

# Get the number of args for a function
def enumerateFunctionArgs(functions):

    function_args_address = []

    for function in functions:
        args = inspect.signature(function[1])
        parameter_count = len(args.parameters) - 1
        function_args_address.append((function[0], parameter_count, function[1]))
       
    return function_args_address

# Check if child object has methods attached to it
def checkChildObject(childObject):
    print(childObject)
    return dir(childObject)

def isPrivate(function):
    if function[0] == "_" and function[1] == "_":
        return True

    if function[0] == "_":
        return True

    return False

def enumerateChildFunctions(lib, functions, childObject):
    function_args_address = []

    for function in functions:
        
        if isPrivate(function):
            continue
        
        if function in vars(childObject):
            continue

        thing = getattr(childObject.__class__, function)
        

        if callable(thing):
            print(thing)
            args = inspect.signature(thing)
            print(args)
       # print(args)
       # parameter_count = len(args.parameters) - 1
       # print(getattr(function))
       # function_args_address.append((function, parameters_count, getattr(function)))
