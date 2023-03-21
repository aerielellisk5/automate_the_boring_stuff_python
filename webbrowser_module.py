import webbrowser, sys, pyperclip

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