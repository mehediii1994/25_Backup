
import getpass
import telnetlib

HOST = "172.16.109.26"
user = input("Enter your remote account: ")
password = getpass.getpass()

try:
    tn = telnetlib.Telnet(HOST)
    
    tn.read_until(b"Username:")
    tn.write(user.encode('ascii') + b"\n")
    
    if password:
        tn.read_until(b"Password:")
        tn.write(password.encode('ascii') + b"\n")
    
    tn.write(b"enable\n")
    tn.write(b"config\n")
    tn.write(b"exit\n")  # Ensure the session ends
    
    print(tn.read_all().decode('ascii'))
except Exception as e:
    print(f"Error: {e}")
"""


