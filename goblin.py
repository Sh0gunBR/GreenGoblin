# Import modules
from pyfiglet import figlet_format
from  termcolor import colored
import whois
import socket
import datetime
import sys
import os
import time

# Rearrange screen
os.system('clear')

# Banner and Signature
print((colored(figlet_format("Green Goblin"), color="green")))
print(colored('By: Sh0gun', color='magenta'))

#Portscanner
target = input(colored('Type domain IP: ', color='yellow'))
print(colored('='  * 50, color='cyan'))
print(colored('Scanning Target: ' + target, color='green'))
print(colored('Scanning starting...', color='green'))
print(colored('='  * 50, color='cyan'))
try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(colored('[ * ] Port {} is open'.format(port), color='blue'))
            s.close( )
except KeyboardInterrupt:
        print(colored('\n Exit...', color='red'))
        sys.exit()
except socket.error:
        print(colored('\n The host is not responding...', color='red'))
        sys.exit()

# Whois lookup
target = whois.whois(target)
data = {

		'expiration_date': datetime.datetime(2020, 9, 14, 0, 0),
		'last_updated': datetime.datetime(2011, 7, 20, 0, 0),
		'registrar': 'MARKMONITOR INC.',
		'name': target,
		'creation_date': datetime.datetime(1997, 9, 15, 0, 0)
	}
print(data)
whois.whois(input(target))
data = {

		'expiration_date': datetime.datetime(2020, 9, 14, 0, 0),
		'last_updated': datetime.datetime(2011, 7, 20, 0, 0),
		'registrar': 'MARKMONITOR INC.',
		'name': target,
		'creation_date': datetime.datetime(1997, 9, 15, 0, 0)
	}
print(data)
