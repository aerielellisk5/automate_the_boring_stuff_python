import webbrowser, sys
import pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

#check if command line arguments were passed

if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] --> ' 870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
# 870 Valencia St, San Francisco, CA 94110
webbrowser.open('https://www.google.com/maps/place/' + address)

# Stuck here because for some odd reason I can import pyperclip.  I've tried editing the default interpreter to match the location of where it is in homebrew, but for some reason that's still 
# not working for me.  Will need to get some help with this

# this was fun - I basically needed to upgrade pip so that the paths matched.
3 #I kept getting stuck in this look here:


# ((name)) automate_the_boring_stuff_python % python3 webbrowser_module.py
# Traceback (most recent call last):
#   File "/Users/aerielellis/Desktop/automate_the_boring_stuff_python/webbrowser_module.py", line 2, in <module>
#     import pyperclip
# ModuleNotFoundError: No module named 'pyperclip'

# ((name)) automate_the_boring_stuff_python % python3 -m pip install --upgrade pip
# Requirement already satisfied: pip in /opt/homebrew/lib/python3.11/site-packages (22.3.1)
# Collecting pip
#   Using cached pip-23.0.1-py3-none-any.whl (2.1 MB)
# Installing collected packages: pip
#   Attempting uninstall: pip
#     Found existing installation: pip 22.3.1
#     Uninstalling pip-22.3.1:
#       Successfully uninstalled pip-22.3.1
# Successfully installed pip-23.0.1