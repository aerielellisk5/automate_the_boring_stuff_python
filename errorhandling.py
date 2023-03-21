

# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('"symbol" needs to a string of length 1.')
#     if (width < 2) or (height < 2):
#         raise Exception('"widht or height is less than 2"')
#     print(symbol * width)
    
#     for i in range(height -2):
#         print(symbol + (' ' * (width - 2)) + symbol)
        
#     print(symbol * width)
    
# # boxPrint('*', 15, 5)
# # boxPrint('O', 5, 16)
    
# boxPrint('O', 1, 16)    

# market_2nd = {'ns' : 'green', 'ew' : 'red'}

# def switchLights(intersection):
#     for key in intersection.keys():
#         if intersection[key] == 'green':
#             intersection[key] = 'yellow'
#         elif intersection == 'yellow':
#             intersection[key] = 'red'
#         elif intersection[key] == 'red':
#             intersection[key] = 'green'
#     assert 'red' in intersection.values(), 'Neither light is red'
# print(market_2nd)            
# switchLights(market_2nd)
# print(market_2nd)  






################

# Type "help", "copyright", "credits" or "license" for more information.
# >>> 42/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>> raise Exception('This is the error message.')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# Exception: This is the error message.
# >>> 
# >>> 
# >>> import traceback
# >>> try: 
# ...     raise Exception('This is an error message')
# ... except:
# ...     errorFile = open('error_log.txt', 'a')
# ...     errorFile.write(traceback.format_exc())
# ...     errorFile.close()
# ... print('The traceback info was written error_log.txt')
#   File "<stdin>", line 7
#     print('The traceback info was written error_log.txt')
#     ^^^^^
# SyntaxError: invalid syntax
# >>> 
# >>>     raise Exception('This is an error message')
#   File "<stdin>", line 1
#     raise Exception('This is an error message')
# IndentationError: unexpected indent
# >>> try:
# ...     raise Exception('This is an error message')
# ...     errorFile = open('error_log.txt', 'a')
# ...     errorFile.write(traceback.format_exc())
# ...     errorFile.close()
# ...     print('The traceback info was written in error_log.txt')
# ... 
#   File "<stdin>", line 7
    
#     ^
# SyntaxError: expected 'except' or 'finally' block
# >>> 
# >>> try:
# ...     raise Exception('This is an error message')
# ...     errorFile = open('error_log.txt', 'a')
# ...     errorFile.write(traceback.format_exc())
# ...     errorFile = open('error_log.txt', 'a')
# ... 
#   File "<stdin>", line 6
    
#     ^
# SyntaxError: expected 'except' or 'finally' block
# >>> 
# >>> try:
# ...     raise Exception('This is an error message')
# ... except:
# ...     errorFile = open('error_log.txt', 'a')
# ...     errorFile.write(traceback.format_exc())
# ...     errorFile.close()
# ...     print('The traceback info was written in error_log.txt')
# ... 
# 109
# The traceback info was written in error_log.txt
# >>> import os
# >>> print(os.getcwd())
# /Users/aerielellis/Desktop/testing
# >>> 
# >>> 
# >>> 
# >>> assert False. 
#   File "<stdin>", line 1
#     assert False. 
#                   ^
# SyntaxError: invalid syntax
# >>> assert False, 'This is an error message'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError: This is an error message
# >>> 
