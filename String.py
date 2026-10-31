#A string is a sequence of characters (letters, digits, spaces, symbols) written inside quotes. 
# It is Python’s data type for text, and its type name is str.

#--------Example of String--------#
str = "PYTHON"
print(str[0])     # P
print(str[3])     # H
print(str[-1])    # N


#--------example of string slicing----#
str = "PYTHON"
print(str[0:3])     # PYT
print(str[2:])      # THON
print(str[:4])      # PYTH
print(str[::-1])    # NOHTYP (reversed)


#----------Example of Case conversion---------#
text = "hello World pYthon"
print(text.upper())         # HELLO WORLD PYTHON
print(text.lower())         # hello world python
print(text.title())         # Hello World Python
print(text.capitalize())    # Hello world python
