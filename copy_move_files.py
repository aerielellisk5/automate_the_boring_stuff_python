# >>> import shutil
# >>> shutil.copy('/Users/aerielellisk5/Desktop/bacon.txt', '/Users/aerielellisk5/Documents')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/opt/homebrew/Cellar/python@3.10/3.10.10/Frameworks/Python.framework/Versions/3.10/lib/python3.10/shutil.py", line 417, in copy
#     copyfile(src, dst, follow_symlinks=follow_symlinks)
#   File "/opt/homebrew/Cellar/python@3.10/3.10.10/Frameworks/Python.framework/Versions/3.10/lib/python3.10/shutil.py", line 254, in copyfile
#     with open(src, 'rb') as fsrc:
# FileNotFoundError: [Errno 2] No such file or directory: '/Users/aerielellisk5/Desktop/bacon.txt'
# >>> print(os.getcwd())
# /Users/aerielellis/Desktop
# >>> shutil.copy('/Users/aerielellis/Desktop/bacon.txt', '/Users/aerielellis/Documents'
# ... )
# '/Users/aerielellis/Documents/bacon.txt'
# >>> shutil.copy('/Users/aerielellis/Desktop/bacon.txt', '/Users/aerielellis/Documents/newbacon.txt')
# '/Users/aerielellis/Documents/newbacon.txt'
# >>> shutil.move('/Users/aerielellis/Desktop/mydata', '/Users/aerielellis/Documents')
# '/Users/aerielellis/Documents/mydata'
# >>> for filename in os.listdir():
# ...     if filename.endswith('.rxt'):
# ...             #os.unlink(filename)
# ...             print(filename)
# ... 
# >>> 
# >>> for filename in os.listdir():
# ...     if filename.endswith('.txt'):
# ...             print(filename)
# ... 
# bacon.txt
# hello2.txt
# hello.txt
# >>> 
# >>> 
# >>> pip.exe install sent2trash
#   File "<stdin>", line 1
#     pip.exe install sent2trash
#             ^^^^^^^
# SyntaxError: invalid syntax
# >>> pip install send2trash
#   File "<stdin>", line 1
#     pip install send2trash
#         ^^^^^^^
# SyntaxError: invalid syntax
# >>> pipinstall send2trash
#   File "<stdin>", line 1
#     pipinstall send2trash
#                ^^^^^^^^^^
# SyntaxError: invalid syntax
# >>> 
# >>> pip install Send2Trash
#   File "<stdin>", line 1
#     pip install Send2Trash
#         ^^^^^^^
# SyntaxError: invalid syntax
# >>> 
# >>> 
# >>> exit()



# >>> import os
# >>> for folder, subfolders, filenames in os.walk('/Users/aerielellis/Desktop/testing')
#   File "<stdin>", line 1
#     for folder, subfolders, filenames in os.walk('/Users/aerielellis/Desktop/testing')
#                                                                                       ^
# SyntaxError: expected ':'
# >>> for folder, subfolders, filenames in os.walk('/Users/aerielellis/Desktop/testing'):
# ...     print('The folder is ' + folder)
# ...     print('The subfolders in ' + folder + ' are: ' + str(subfolders))
# ...     print('The filenames in ' + folder + ' are: ' + str(filenames))
# ...     print()
# ... 
# The folder is /Users/aerielellis/Desktop/testing
# The subfolders in /Users/aerielellis/Desktop/testing are: ['noname1', 'noname2']
# The filenames in /Users/aerielellis/Desktop/testing are: ['file2.txt', 'file3.txt', 'file1.txt']

# The folder is /Users/aerielellis/Desktop/testing/noname1
# The subfolders in /Users/aerielellis/Desktop/testing/noname1 are: ['inside_noname1']
# The filenames in /Users/aerielellis/Desktop/testing/noname1 are: ['no.txt', 'name.txt']

# The folder is /Users/aerielellis/Desktop/testing/noname1/inside_noname1
# The subfolders in /Users/aerielellis/Desktop/testing/noname1/inside_noname1 are: []
# The filenames in /Users/aerielellis/Desktop/testing/noname1/inside_noname1 are: []

# The folder is /Users/aerielellis/Desktop/testing/noname2
# The subfolders in /Users/aerielellis/Desktop/testing/noname2 are: []
# The filenames in /Users/aerielellis/Desktop/testing/noname2 are: ['nonames.txt', 'nonames123.txt']

# >>> 

