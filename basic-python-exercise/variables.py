# A python variable name must start with a letter or the underscore character

program_name = "python variable"
_program_name = "python variable"

print(program_name)
print(_program_name)

# This line will give an error because the variable name is starting with a number
# 1programname = "python code"

# variable name can only contain alpha-numeric characters and underscores
# (A-z, 0-9, and _)

_name1 = "printing (_name1) variable"
print(_name1)

# this line will give an error
# _name@1 = "name variable"

# case-sensitive
# the name, Name are two different variables
name = "printing (name) variable..."
Name = "printing (Name) variable..."
print(name)
print(Name)
# reserved words cannot be used as variables
# error at below code
# class = "printing (class) variable"
