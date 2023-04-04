# this one was a little tricky because gmail has updated the way that they do things.  So basically, I kept getting an authentication error saying that my username and password were not accepted.  i tried creating a new email + password.  That still didnt work.  Turns out you need a special "app password" that is used for less secure apps.  Weird thing was, you had to turn on 2-factor authentication in order to get access to the "app password".  And even then, when I chose "mac" as my option, since I'm on a macbook, it still didnt sign me in.  I had to use the "other", option, and it finally worked! 

# >>> import smtplib
# >>> conn = smtplib.SMTP('smpt.gmail.com', 587)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 255, in __init__
#     (code, msg) = self.connect(host, port)
#                   ^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 341, in connect
#     self.sock = self._get_socket(host, port, self.timeout)
#                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 312, in _get_socket
#     return socket.create_connection((host, port), timeout,
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socket.py", line 827, in create_connection
#     for res in getaddrinfo(host, port, 0, SOCK_STREAM):
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socket.py", line 962, in getaddrinfo
#     for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# socket.gaierror: [Errno 8] nodename nor servname provided, or not known
# >>> conn = smtplib.SMTP('smtp.gmail.com', 587)
# >>> conn
# <smtplib.SMTP object at 0x105764750>
# >>> conn.ehlo()
# (250, b'smtp.gmail.com at your service, [2601:644:8f01:7ae0:c86:34ab:f6c3:7213]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
# >>> conn.starttls()
# (220, b'2.0.0 Ready to start TLS')
# >>> conn.login('kawasaki.aeriel', 'eab*uhp3tvb9ZRG0bfp')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 750, in login
#     raise last_exception
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 739, in login
#     (code, resp) = self.auth(
#                    ^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 662, in auth
#     raise SMTPAuthenticationError(code, resp)
# smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials u4-20020a170902bf4400b001a27f810a2esm3542035pls.256 - gsmtp')
# >>> conn.login('kawasakiaeriel@gmail.com', 'qqflbeeqiyltteeb')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 739, in login
#     (code, resp) = self.auth(
#                    ^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 642, in auth
#     (code, resp) = self.docmd("AUTH", mechanism + " " + response)
#                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 432, in docmd
#     return self.getreply()
#            ^^^^^^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 405, in getreply
#     raise SMTPServerDisconnected("Connection unexpectedly closed")
# smtplib.SMTPServerDisconnected: Connection unexpectedly closed
# >>> conn.login('kawasakiaeriel@gmail.com', 'uovvzilpzurmrphk')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 739, in login
#     (code, resp) = self.auth(
#                    ^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 642, in auth
#     (code, resp) = self.docmd("AUTH", mechanism + " " + response)
#                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 431, in docmd
#     self.putcmd(cmd, args)
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 378, in putcmd
#     self.send(f'{s}{CRLF}')
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 365, in send
#     raise SMTPServerDisconnected('please run connect() first')
# smtplib.SMTPServerDisconnected: please run connect() first
# >>> SMTP.connect(host='localhost', port=0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'SMTP' is not defined
# >>> con
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'con' is not defined. Did you mean: 'conn'?
# >>> conn
# <smtplib.SMTP object at 0x105764750>
# >>> conn.connect()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 341, in connect
#     self.sock = self._get_socket(host, port, self.timeout)
#                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 312, in _get_socket
#     return socket.create_connection((host, port), timeout,
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socket.py", line 851, in create_connection
#     raise exceptions[0]
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socket.py", line 836, in create_connection
#     sock.connect(sa)
# ConnectionRefusedError: [Errno 61] Connection refused
# >>> exit()
# aerielellis@AerielPerson ~ % python3
# Python 3.11.2 (main, Feb 16 2023, 02:55:59) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import smtplib
# >>> conn = smtplib.SMTP('smtp.gmail.com', 587)
# >>> conn.ehlo()
# (250, b'smtp.gmail.com at your service, [2601:644:8f01:7ae0:c86:34ab:f6c3:7213]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
# >>> conn.starttls()
# (220, b'2.0.0 Ready to start TLS')
# >>> conn.login('kawasakiaeriel@gmail.com', 'qqflbeeqiyltteeb')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 750, in login
#     raise last_exception
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 739, in login
#     (code, resp) = self.auth(
#                    ^^^^^^^^^^
#   File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/smtplib.py", line 662, in auth
#     raise SMTPAuthenticationError(code, resp)
# smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials b11-20020a170902ed0b00b001a22d274045sm3601169pld.144 - gsmtp')
# >>> conn.login('kawasakiaeriel@gmail.com', 'FINALLY WORKED CORRECTLY')
# (235, b'2.7.0 Accepted')



# >>> conn
# <smtplib.SMTP object at 0x1049e8ed0>
# >>> conn.ehlo()
# (250, b'smtp.gmail.com at your service, [2601:644:8f01:7ae0:c86:34ab:f6c3:7213]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
# >>> conn.starttls()
# (220, b'2.0.0 Ready to start TLS')
# >>> conn.login('kawasakiaeriel@gmail.com', 'PASSWORD HERE')
# (235, b'2.7.0 Accepted')
# >>> conn.sendmail('kawasakiaeriel@gmail.com', 'kawasakiaeriel@gmail.com', 'Subject: A subject goes here . \n\nDear Aeriel, thank you for the fun \n\n -Aeriel')
# {}
# >>> conn.quit()
# (221, b'2.0.0 closing connection y8-20020aa78548000000b006288ca3cadfsm3921901pfn.35 - gsmtp')
# >>> 


import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)