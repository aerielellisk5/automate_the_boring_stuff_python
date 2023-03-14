# Last login: Tue Feb 28 12:42:43 on ttys000
# complete:13: command not found: compdef
# aerielellis@AerielPerson ~ % python3
# Python 3.10.10 (main, Feb  8 2023, 05:32:04) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import re
# >>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# >>> phoneNumRegex.search('My number is 415-555-4242')
# <re.Match object; span=(13, 25), match='415-555-4242'>
# >>> mo = phoneNumRegex.search('My number is 415-555-4242')
# >>> mo.group()
# '415-555-4242'
# >>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# >>> mo.grou()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 're.Match' object has no attribute 'grou'. Did you mean: 'group'?
# >>> mo.group()
# '415-555-4242'
# >>> mo.group(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: no such group
# >>> mo.group(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: no such group
# >>> mo.group()
# '415-555-4242'
# >>> mo = phoneNumRegex.search('My number is 415-555-4242')
# >>> mo.group()
# '415-555-4242'
# >>> go.group(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'go' is not defined. Did you mean: 'mo'?
# >>> mo.group(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: no such group
# >>> clear
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'clear' is not defined
# >>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# >>> mo = phoneNumRegex.search('My number is 415-555-4242')
# >>> mo.group()
# '415-555-4242'
# >>> mo.group(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: no such group
# >>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# >>> mo = phoneNumRegex.search('My number is 415-555-4242')
# >>> mo group()
#   File "<stdin>", line 1
#     mo group()
#        ^^^^^
# SyntaxError: invalid syntax
# >>> mo.group()
# '415-555-4242'
# >>> mo.group(1)
# '415'
# >>> mo.group(2)
# '555-4242'
# >>> phoneNumRegex = re.complile(r'/(\d\d\d) \d\d\d-\d\d\d\d')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 're' has no attribute 'complile'. Did you mean: 'compile'?
# >>> phoneNumRegex = re.compile(r'/(\d\d\d) \d\d\d-\d\d\d\d')
# >>> mo = phoneNumRegex.search('My number is (415)-555-4242')
# >>> mo.group()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'
# >>> mo = phoneNumRegex.search('My number is (415)-555-4242')
# >>> mo = phoneNumRegex.search('My number is (415) 555-4242')
# >>> mo.group()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'
# >>> 
# >>> 
# >>> 
# >>> batRegex = re.complile(r'Bat(man|mobile|copter|bat)')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 're' has no attribute 'complile'. Did you mean: 'compile'?
# >>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# >>> mo = batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# >>> mo = batRegex.search('Batmobile lost a wheel')
# >>> mo.group()
# 'Batmobile'
# >>> mo.group1)
#   File "<stdin>", line 1
#     mo.group1)
#              ^
# SyntaxError: unmatched ')'
# >>> mo.group(1)
# 'mobile'
# >>> 
# >>> 
# >>> 
# >>> batRegex = re.compile(r'Bat(wo)?man')
# >>> mo = batRegex.search('The adventures of Batman')
# >>> mo.group()
# 'Batman'
# >>> mo.group(1)
# >>> 
# >>> mo = batRegex.search('The adventures of Batwoman')
# >>> mo.group()
# 'Batwoman'
# >>> mo = batRegex.search('The adventures of Batwowowowowman')
# >>> phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# >>> phoneRegex.search('My new phone number is 123-456-7890')
# <re.Match object; span=(23, 35), match='123-456-7890'>
# >>> mo.group()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'
# >>> mo = phoneRegex.search('My new phone number is 123-456-7890')
# >>> mo.group()
# '123-456-7890'
# >>> 
# >>> 
# >>> batRegex = re.compile(r'Bat(wo)?man')
# >>> mo.group
# <built-in method group of re.Match object at 0x100586ec0>
# >>> mo.group()
# '123-456-7890'
# >>> mp = batRegex.search('The adventures of Batman')
# >>> mo = batRegex.search('The adventures of Batman')
# >>> mo.group()
# 'Batman'
# >>> mo = batRegex.search('The adventures of Batwowowowman')
# >>> mo == None
# True
# >>> phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# >>> mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
# >>> mo.group()
# '415-555-1234'
# >>>  phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
#   File "<stdin>", line 1
#     phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
# IndentationError: unexpected indent
# >>> phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
# <re.Match object; span=(19, 31), match='415-555-1234'>
# >>> phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
# >>> phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
# >>> phoneRegex = re.compile(r'(\d\d\d)?\d\d\d=\d\d\d\d')
# >>> phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
# >>> phoneRegex = re.compile(r'(\d\d\d)?\d\d\d-\d\d\d\d')
# >>> phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
# <re.Match object; span=(19, 27), match='555-1234'>
# >>> phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
# <re.Match object; span=(23, 31), match='555-1234'>
# >>> 
# >>> 
# >>> 
# >>> 
# >>> batRegex = re.compile(r'Bat(wo)?man')
# >>> mo = batRegex.search('The adventures of Batwowowowman')
# >>> batRegex = re.compile(r'Bat(wo)*man')
# >>> mo = batRegex.search('The adventures of Batwowowowman')
# >>> mo = batRegex.search('The adventures of Batwoman')
# >>> batRegex.search('The adventures of Batwoman')
# <re.Match object; span=(18, 26), match='Batwoman'>
# >>> batRegex.search('The adventures of Batwowowowman')
# >>> batRegex = re.compile(r'Bat(wo)*man')
# >>> batRegex.search('The adventures of Batwowowowman')
# >>> batRegex.search('The adventures of Batwowowowman')
# >>> batRegex.search('The adventures of Batwowowowman')
# >>> batRegex.search('The adventures of Batwowowowman')
# >>> batRegex.search('The adventures of Batwoman')
# <re.Match object; span=(18, 26), match='Batwoman'>
# >>> batRegex.search('The adventures of Batman')
# <re.Match object; span=(18, 24), match='Batman'>
# >>> batRegex.search('The adventures of Batwowoman')
# <re.Match object; span=(18, 28), match='Batwowoman'>
# >>> batRegex.search('The adventures of Batwowowowowoman')
# <re.Match object; span=(18, 34), match='Batwowowowowoman'>
# >>> batRegex.search('The adventures of Batwowowowowoman')
# <re.Match object; span=(18, 34), match='Batwowowowowoman'>
# >>> 
# >>> 
# >>> 
# >>> 
# >>> batRegex = re.compile(r'Bat(wo)+man')
# >>> batRegex.search('The Adventures of Batman')
# >>> batRegex.search('The Adventures of Batwoman')
# <re.Match object; span=(18, 26), match='Batwoman'>
# >>> batRegex.search('The adventures of Batwowowowowoman')
# <re.Match object; span=(18, 34), match='Batwowowowowoman'>
# >>> 
# >>> 
# >>> 
# >>> regex = re.compile(r'\+\*\?')
# >>> regex.search(I learned about +*? regex syntax')
#   File "<stdin>", line 1
#     regex.search(I learned about +*? regex syntax')
#                  ^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# >>> regex.search('I learned about +*? regex syntax')
# <re.Match object; span=(16, 19), match='+*?'>
# >>> 
# >>> 
# >>> 
# >>> haRegex = re.compile(r'(Ha){3}')
# >>> haRegex.search('He said "HaHaHa"')
# <re.Match object; span=(9, 15), match='HaHaHa'>
# >>> phoneRegex.search(r'(\d\d\d-)?\d\d\d\-\d\d\d\d(,)? {3}')
# >>> phoneRegex.search('My numbers are 415-555-1234, 555-1234, 212-555-0000')
# <re.Match object; span=(19, 27), match='555-1234'>
# >>> phoneRegex.search('My numbers are 415-555-1234, 555-1234, 212-555-000')
# <re.Match object; span=(19, 27), match='555-1234'>
# >>> phoneRegex.search(r'((\d\d\d-)?\d\d\d\-\d\d\d\d(,)? {3}')
# >>> phoneRegex.search('My numbers are 415-555-1234, 555-1234, 212-555-0000')
# <re.Match object; span=(19, 27), match='555-1234'>
# >>> phoneRegex.search(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)? {3}')
# >>> phoneRegex.search('My numbers are 415-555-1234, 555-1234, 212-555-0000')
# <re.Match object; span=(19, 27), match='555-1234'>
# >>> phoneRegex.search(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?) {3}')
# >>> phoneRegex.search('My numbers are 415-555-1234, 555-1234, 212-555-0000')
# <re.Match object; span=(19, 27), match='555-1234'>
# >>> phoneRegex.search(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
# >>> phoneRegex.search('My numbers are 415-555-1234, 555-1234, 212-555-0000')
# <re.Match object; span=(19, 27), match='555-1234'>
# >>> phoneRegex.search(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
# >>> phoneRegex.search('My numbers are 415-555-1234, 555-1234, 212-555-0000')
# <re.Match object; span=(19, 27), match='555-1234'>
# >>> 
# >>> 
# >>> 
# >>> phoneRegex.search(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
# >>> phoneRegex.search('My numbers are 415-555-1234,555-1234,212-555-0000')
# <re.Match object; span=(19, 27), match='555-1234'>
# >>> 
# >>> 
# >>> 
# >>> phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
# >>> phoneRegex.search('Mynumbers are 415-555-1234,555-1234,212-555-0000')
# <re.Match object; span=(14, 48), match='415-555-1234,555-1234,212-555-0000'>
# >>> digitRegex =  re.compile('r(\d){3,5}')
# >>> digitRegex.search('1234567890')
# >>> 
# >>> 
# >>> 
# >>> digitRegex =  re.compile(r'(\d){3,5}')
# >>> digitRegex.search('1234567890')
# <re.Match object; span=(0, 5), match='12345'>
# >>> digitRegex =  re.compile(r'(\d){3,5}?')
# >>> digitRegex.search('1234567890')
# <re.Match object; span=(0, 3), match='123'>
# >>> 
# >>> 
# >>> 
# >>> phonneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# >>> phonneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# >>> 
# >>> 
# >>> 
# >>> 
# >>> lyriccs = 'On the first day of Christmas my true love sent to me
#   File "<stdin>", line 1
#     lyriccs = 'On the first day of Christmas my true love sent to me
#               ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> A partridge in a pear tree
#   File "<stdin>", line 1
#     A partridge in a pear tree
#       ^^^^^^^^^
# SyntaxError: invalid syntax
# >>> 
# >>> On the second day of Christmas my true love sent to me
#   File "<stdin>", line 1
#     On the second day of Christmas my true love sent to me
#        ^^^
# SyntaxError: invalid syntax
# >>> Two turtle doves,
#   File "<stdin>", line 1
#     Two turtle doves,
#         ^^^^^^
# SyntaxError: invalid syntax
# >>> And a partridge in a pear tree.
#   File "<stdin>", line 1
#     And a partridge in a pear tree.
#         ^
# SyntaxError: invalid syntax
# >>> 
# >>> On the third day of Christmas my true love sent to me
#   File "<stdin>", line 1
#     On the third day of Christmas my true love sent to me
#        ^^^
# SyntaxError: invalid syntax
# >>> Three French hens,
#   File "<stdin>", line 1
#     Three French hens,
#           ^^^^^^
# SyntaxError: invalid syntax
# >>> Two turtle doves,
#   File "<stdin>", line 1
#     Two turtle doves,
#         ^^^^^^
# SyntaxError: invalid syntax
# >>> lyrics = ''' On the first day of Christmas my true love sent to me
# ... A partridge in a pear tree
# ... 
# ... On the second day of Christmas my true love sent to me
# ... Two turtle doves,
# ... And a partridge in a pear tree.
# ... 
# ... On the third day of Christmas my true love sent to me
# ... Three French hens,
# ... Two turtle doves,
# ... And a partridge in a pear tree.
# ... '''
# >>> print(lyrics)
#  On the first day of Christmas my true love sent to me
# A partridge in a pear tree

# On the second day of Christmas my true love sent to me
# Two turtle doves,
# And a partridge in a pear tree.

# On the third day of Christmas my true love sent to me
# Three French hens,
# Two turtle doves,
# And a partridge in a pear tree.

# >>> 
# >>> 
# >>> 
# >>> xmasRegex = re.compile(r'\d+\s\w+')
# >>> xmasRegex.findall(lyrics)
# []
# >>> lyrics = '12 drumers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing,8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'
# >>> xmasRegex.findall(lyrics)
# ['12 drumers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 golden', '4 calling', '3 french', '2 turtle', '1 partridge']
# >>> 
# >>> 
# >>> 
# >>> vowelRegex = re.compile(r'[aeiou]')
# >>> vowelRegex = re.compile(r'[aeiouAEIOU]')
# >>> xmasRegex.findall(lyrics)
# ['12 drumers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 golden', '4 calling', '3 french', '2 turtle', '1 partridge']
# >>> vowelRgex = re.compile(r'[aeiouAEIOU]')
# >>> vowelRegex = re.compile(r'[aeiouAEIOU]')
# >>> vowelRegex.findall('Robocop eats baby food')
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']
# >>> doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
# >>> doubleVowelRegex.findall('Robocop eats baby food')
# ['ea', 'oo']
# >>> 
# >>> 
# >>> 
# >>> vowelRegex = re.compile(r'[^aeiouAEIOU]')
# >>> vowelRegex.findall('Robocop eats baby food')
# ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd']
# >>> vowelRegex = re.compile(r'[^aeiouAEIOU ]')
# >>> vowelRegex.findall('Robocop eats baby food')
# ['R', 'b', 'c', 'p', 't', 's', 'b', 'b', 'y', 'f', 'd']
# >>> 
# >>> 
# >>> 
# >>> beginsWithHelloRegex = re.compile(r'^Hello')
# >>> beginsWithHelloRegex.search('Hello there')
# <re.Match object; span=(0, 5), match='Hello'>
# >>> beginsWithHelloRegex.search('He said Hello there')
# >>> endsWithWorldRegex = re.compile(r'world!$')
# >>> endsWithWorldRegex.search('hello world!')
# <re.Match object; span=(6, 12), match='world!'>
# >>> endsWithWorldRegex.search('hello world!wef\')
#   File "<stdin>", line 1
#     endsWithWorldRegex.search('hello world!wef\')
#                               ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> endsWithWorldRegex.search('hello world!wef')
# >>> 
# >>> 
# >>> allDigitsRege = re.compile(r'^\d+$)
#   File "<stdin>", line 1
#     allDigitsRege = re.compile(r'^\d+$)
#                                ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> allDigitsRege = re.compile(r'^\d+$')
# >>> allDigitsRege.search('2340923409234')
# <re.Match object; span=(0, 13), match='2340923409234'>
# >>> allDigitsRege.search('23409234092s34')
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> atRegex = re.compile(r'.at')
# >>> atRegex.findall(
# ... 
# KeyboardInterrupt
# >>> atRegex.findall('The cat in the hate sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat']
# >>> atRegex = re.compile(r'.{1,2}')
# >>> atRegex.findall('The cat in the hate sat on the flat mat.')
# ['Th', 'e ', 'ca', 't ', 'in', ' t', 'he', ' h', 'at', 'e ', 'sa', 't ', 'on', ' t', 'he', ' f', 'la', 't ', 'ma', 't.']
# >>> 
# >>> 
# >>> 
# >>> 'First Name: All Last Name: Sweigart'
# 'First Name: All Last Name: Sweigart'
# >>> 
# >>> 
# >>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# >>> nameRegex.findall('First Name: All Last Name: Sweigart')
# [('All', 'Sweigart')]
# >>> 
# >>> 
# >>> 
# >>> serve = '<To serve humans> for dinner.>'
# >>> nongreed = re.compile(r'<(.*?)>')
# >>> nongreedy.findall(serve)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'nongreedy' is not defined. Did you mean: 'nongreed'?
# >>> nongreed.findall(serve)
# ['To serve humans']
# >>> 
# >>> 
# >>> greedy = re.compile(r'<(.*)>')
# >>> greedy.findall(serve)
# ['To serve humans> for dinner.']
# >>> 
# >>> 
# >>> prime = 'Serve the public trust. \nProtect the innocent \nUpload the law'
# >>> print(prime)
# Serve the public trust. 
# Protect the innocent 
# Upload the law
# >>> dotStar = re.compile(r'.*')
# >>> dosStar.search(prime)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'dosStar' is not defined. Did you mean: 'dotStar'?
# >>> dotStar.search(prime)
# <re.Match object; span=(0, 24), match='Serve the public trust. '>
# >>> dotStar = re.compile(r'.*', reDOTALL)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'reDOTALL' is not defined
# >>> dotStar = re.compile(r'.*', re.DOTALL)
# >>> dotStar.search(prime)
# <re.Match object; span=(0, 61), match='Serve the public trust. \nProtect the innocent \n>
# >>> 
# >>> 
# >>> 
# >>> vowelRegex = re.compile(r'[aeious]')
# >>> vowelRegex.search('Al, why does your programming book talk about RoboCop so much?')
# <re.Match object; span=(9, 10), match='o'>
# >>> vowelRegex = re.compile(r'[aeiou]')
# >>> vowelRegex.search('Al, why does your programming book talk about RoboCop so much?')
# <re.Match object; span=(9, 10), match='o'>
# >>> vowelRegex.findAll('Al, why does your programming book talk about RoboCop so much?')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 're.Pattern' object has no attribute 'findAll'. Did you mean: 'findall'?
# >>> vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
# ['o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u']
# >>> vowelRegex = re.compile(r'[aeiou]', re.I)
# >>> vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
# ['A', 'o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u']
# >>> 
# >>> 
# >>> 
# >>> namesRegex = re.compile(r'(Agent \w+')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/opt/homebrew/Cellar/python@3.10/3.10.10/Frameworks/Python.framework/Versions/3.10/lib/python3.10/re.py", line 251, in compile
#     return _compile(pattern, flags)
#   File "/opt/homebrew/Cellar/python@3.10/3.10.10/Frameworks/Python.framework/Versions/3.10/lib/python3.10/re.py", line 303, in _compile
#     p = sre_compile.compile(pattern, flags)
#   File "/opt/homebrew/Cellar/python@3.10/3.10.10/Frameworks/Python.framework/Versions/3.10/lib/python3.10/sre_compile.py", line 788, in compile
#     p = sre_parse.parse(p, flags)
#   File "/opt/homebrew/Cellar/python@3.10/3.10.10/Frameworks/Python.framework/Versions/3.10/lib/python3.10/sre_parse.py", line 955, in parse
#     p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
#   File "/opt/homebrew/Cellar/python@3.10/3.10.10/Frameworks/Python.framework/Versions/3.10/lib/python3.10/sre_parse.py", line 444, in _parse_sub
#     itemsappend(_parse(source, state, verbose, nested + 1,
#   File "/opt/homebrew/Cellar/python@3.10/3.10.10/Frameworks/Python.framework/Versions/3.10/lib/python3.10/sre_parse.py", line 843, in _parse
#     raise source.error("missing ), unterminated subpattern",
# re.error: missing ), unterminated subpattern at position 0
# >>> namesRegex = re.compile(r''Agent \w+')
#   File "<stdin>", line 1
#     namesRegex = re.compile(r''Agent \w+')
#                                       ^
# SyntaxError: unexpected character after line continuation character
# >>> namesRegex = re.compile(r'Agent \w+')
# >>> namesRegex = findall('Agent Alice gave the secret documents to Agent Bob')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'findall' is not defined
# >>> namesRegex.findall('Agent Alice gave the secret documents to Agent Bob')
# ['Agent Alice', 'Agent Bob']
# >>> namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob')
# 'REDACTED gave the secret documents to REDACTED'
# >>> 
# >>> 
# >>> 
# >>> namesRegex = re.compile(r'Agent (\w)\w*')
# >>> namesRegex.findall('Agent Alice gave the secret documents to Agent Bob')
# ['A', 'B']
# >>> namesRegex.sub(r'Agent \1****','Agent Alice gave the secret documents to Agent Bob')
# 'Agent A**** gave the secret documents to Agent B****'
# >>> 
# >>> 
# >>> 
# >>> 
# >>> re.compile(r'\d\d\d(-)?\d\d\d-\d\d\d\d')
# re.compile('\\d\\d\\d(-)?\\d\\d\\d-\\d\\d\\d\\d')
# >>> re.compile(r'''\d\d\d(-)?\d\d\d-\d\d\d\d', re.VERBOSE)
# ... 
#   File "<stdin>", line 1
#     re.compile(r'''\d\d\d(-)?\d\d\d-\d\d\d\d', re.VERBOSE)
#                ^
# SyntaxError: unterminated triple-quoted string literal (detected at line 1)
# >>> re.compile(r'''
# ... \d\d\d
# ... -
# ... \d\d\d
# ... -
# ... \d\d\d\d'''
# ... , re.VERBOSE)
# re.compile('\n\\d\\d\\d\n-\n\\d\\d\\d\n-\n\\d\\d\\d\\d', re.VERBOSE)